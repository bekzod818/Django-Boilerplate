from rest_framework import serializers

from apps.common import models


class FrontendTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FrontendTranslation
        fields = ("key", "text")
