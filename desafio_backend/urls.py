from django.contrib import admin
from django.urls import path, include

from apps.accounts.auth_views import (
    CustomTokenObtainPairView,
)
from .api_routers import routes
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/signin/', CustomTokenObtainPairView.as_view(), name='signin'),
    path('api/v1/', include(routes)),
]
