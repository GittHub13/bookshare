from django.urls import path, include  # Added include here
from . import views as web_views
from .api import urls as api_urls

urlpatterns = [
    # Web views
    path('profile/', web_views.profile, name='profile'),
    path('register/', web_views.register, name='register'),
    path('login/', web_views.login_view, name='login'),
    path('logout/', web_views.logout_view, name='logout'),

    # API views
    path('api/', include(api_urls)),  # Now include is properly imported
]