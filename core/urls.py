from captcha import fields
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm
from django.urls import include, path

from .schema import swagger_urlpatterns


class LoginForm(AuthenticationForm):
    captcha = fields.ReCaptchaField()

    def clean(self):
        captcha = self.cleaned_data.get("captcha")
        if not captcha:
            return
        return super().clean()


admin.site.login_form = LoginForm
admin.site.login_template = "login.html"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/common/", include("apps.common.urls", namespace="common")),
]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
