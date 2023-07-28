from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import user_registration

urlpatterns = [
    path('register/', user_registration, name='user-registration'),
    path('login/', TokenObtainPairView.as_view(),
         name='token-obtain-pair'),  # Obtain token (login)
    path('token/refresh/', TokenRefreshView.as_view(),
         name='token-refresh'),  # Refresh token
    path('token/verify/', TokenVerifyView.as_view(),
         name='token-verify'),  # Verify token
]
