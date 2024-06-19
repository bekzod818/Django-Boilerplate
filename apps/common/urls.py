from django.urls import path

from .api_endpoints import FrontendTranslationView, VersionHistoryView
from apps.common.views import health_check_celery, health_check_redis

app_name = "common"

urlpatterns = [
    path(
        "FrontendTranslations/",
        FrontendTranslationView.as_view(),
        name="frontend-translations",
    ),
    path("VersionHistory/", VersionHistoryView.as_view(), name="version-history"),
    path("HealthCheck/Redis/", health_check_redis, name="health-check-redis"),
    path("HealthCheck/Celery/", health_check_celery, name="health-check-celery"),
]
