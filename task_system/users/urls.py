from django.urls import path
# from rest_framework.authtoken.views import obtain_auth_token

from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView
)

from users.views import RegisterUserView



urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='token_register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
