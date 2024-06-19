import redis
from celery import Celery
from celery.exceptions import OperationalError
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")

# Configure Redis connection
redis_client = redis.StrictRedis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
)


@api_view(["GET"])
def health_check_redis(request):
    try:
        # Check Redis connection
        redis_client.ping()
        return Response({"status": "success", "message": "Redis server is working now."}, status=status.HTTP_200_OK)
    except redis.ConnectionError:
        return Response(
            {"status": "error", "message": "Redis server is not working."},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["GET"])
def health_check_celery(request):
    try:
        # Ping Celery workers
        response = app.control.ping()
        if response:
            return Response(
                {"status": "success", "workers": response}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"status": "error", "message": "No Celery workers responded."},
                status=status.HTTP_400_BAD_REQUEST,
            )
    except OperationalError:
        return Response(
            {"status": "error", "message": "Celery OperationalError occurred."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
