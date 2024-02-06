import operator
from functools import reduce
from typing import List

from django.db.models import Q
from rest_framework.compat import distinct
from rest_framework.filters import SearchFilter

from apps.text_services import cyrillic_latin_translator
from apps.text_services.q_processors import QLatinCyrillicProcessor


class MultiSymbolSearchFilter(SearchFilter):
    @staticmethod
    def process_terms(
        processor: QLatinCyrillicProcessor, terms: List[str], orm_lookups: List[str]
    ) -> List[Q]:
        joined_terms = " ".join(terms)
        processed_terms = processor.process(joined_terms).split(" ")
        return [
            Q(**{orm_lookup: term})
            for term in processed_terms
            for orm_lookup in orm_lookups
        ]

    def filter_queryset(self, request, queryset, view):
        search_fields = self.get_search_fields(view, request)
        search_terms = self.get_search_terms(request)

        if not search_fields or not search_terms:
            return queryset

        latin_processor = QLatinCyrillicProcessor(cyrillic_latin_translator.LATIN)
        cyrillic_processor = QLatinCyrillicProcessor(cyrillic_latin_translator.CYRILLIC)

        orm_lookups = [
            self.construct_search(str(search_field)) for search_field in search_fields
        ]
        base = queryset
        latin_conditions = self.process_terms(
            latin_processor, search_terms, orm_lookups
        )
        cyrillic_conditions = self.process_terms(
            cyrillic_processor, search_terms, orm_lookups
        )

        combined_latin_conditions = reduce(operator.and_, latin_conditions)
        combined_cyrillic_conditions = reduce(operator.and_, cyrillic_conditions)

        queryset = queryset.filter(
            Q(combined_latin_conditions) | Q(combined_cyrillic_conditions)
        )
        if self.must_call_distinct(queryset, search_fields):
            queryset = distinct(queryset, base)

        return queryset
