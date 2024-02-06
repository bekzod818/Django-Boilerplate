from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.common import models

from . import serializers


class FrontendTranslationView(ListAPIView):
    serializer_class = serializers.FrontendTranslationSerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="key",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Key",
            )
        ]
    )
    def get(self, request):
        # translation.activate(lang)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        data = {}
        for obj in serializer.data:
            data[obj["key"]] = obj["text"]
        return Response(data, status=status.HTTP_200_OK)

    def get_queryset(self):
        queryset = models.FrontendTranslation.objects.all()
        key = self.request.GET.get("key", None)

        if key:
            queryset = queryset.filter(key__icontains=key)

        return queryset
