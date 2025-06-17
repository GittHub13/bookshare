"""
URL configuration for bookshare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static


schema_view: 'drf_yasg.views.SchemeView' = get_schema_view(
    openapi.Info(
        title="BookShare API",
        default_version='v1',
        description="Public API for book sharing",
        contact=openapi.Contact(email="support@bookshare.ge"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Core URLs
    path('', RedirectView.as_view(url='swagger/', permanent=True)),

    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),

    # Admin
    path('admin/', admin.site.urls),

    # API Documentation
    path('swagger/',
         schema_view.with_ui('swagger', cache_timeout=0),  # type: ignore[attr-defined]
         name='schema-swagger-ui'),
    path('swagger.json',
         schema_view.without_ui(cache_timeout=0),  # type: ignore[attr-defined]
         name='schema-json'),
    path('redoc/',
         schema_view.with_ui('redoc', cache_timeout=0),  # type: ignore[attr-defined]
         name='schema-redoc'),

    # API v1 Endpoints
    path('api/v1/', include([
        # Authentication
        path('auth/', include('authentication.urls')),

        # JWT Endpoints
        path('auth/token', TokenObtainPairView.as_view(), name='token-obtain'),
        path('auth/token/refresh', TokenRefreshView.as_view(), name='token-refresh'),

        # Resources
        path('users/', include('users.urls')),
        path('books/', include('books.urls')),
    ])),

    # Health check
    path('health', lambda r: HttpResponse('OK'), name='health-check'),
]