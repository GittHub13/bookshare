from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.http import HttpResponse

schema_view = get_schema_view(
    openapi.Info(
        title="BookShare API",
        default_version='v1',
        description="საჯარო API წიგნების გაზიარებისთვის",
        contact=openapi.Contact(email="support@bookshare.ge"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Redirect root to Swagger
    path('', RedirectView.as_view(url='swagger/', permanent=True)),

    # Admin
    path('admin/', admin.site.urls),

    # JWT auth directly under auth/
    path('api/v1/auth/token/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('api/v1/auth/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),

    # App-specific includes
    path('api/v1/auth/', include('authentication.urls')),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/books/', include('books.urls')),

    # Health check
    path('health/', lambda r: HttpResponse('OK'), name='health-check'),

    # Swagger & ReDoc
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

