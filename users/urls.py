from django.urls import path
from .views import RegisterView, LogoutView, ValidateOTPView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("api/register/", RegisterView.as_view(), name="sign_up"),
    path("api/activate/", ValidateOTPView.as_view(), name="activate"),
    path('api/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', LogoutView.as_view(), name='logout')
]
