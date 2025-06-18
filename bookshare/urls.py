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
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from books import views as book_views
from accounts import views as account_views

schema_view = get_schema_view(
    openapi.Info(
        title="BookShare API",
        default_version='v1',
        description="API for book sharing service",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@bookshare.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),

    # Home Page (Main Landing)
    path('', book_views.home, name='home'),

    # Swagger API Docs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='api-redoc'),

    # API Auth (JWT)
    path('api/v1/auth/', include([
        path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
        path('', include('accounts.api.urls')),
    ])),

    # API Resources
    path('api/v1/', include('books.api.urls')),

    # Books (Web Interface)
    path('books/', include([
        path('', book_views.book_list, name='book-list'),
        path('<int:pk>/', book_views.book_detail, name='book-detail'),
        path('add/', book_views.book_create, name='book-create'),
        path('<int:pk>/edit/', book_views.book_update, name='book-update'),
        path('<int:pk>/delete/', book_views.book_delete, name='book-delete'),
    ])),

    # User Accounts (Web Pages)
    path('accounts/', include([
        path('profile/', account_views.profile, name='profile'),
        path('register/', account_views.register, name='register'),
        path('login/', account_views.login_view, name='login'),
        path('logout/', account_views.logout_view, name='logout'),
    ])),
]

# Static & Media files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)