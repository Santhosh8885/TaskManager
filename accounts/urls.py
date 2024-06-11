from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    path('register/', views.UserRegistrationAPIView.as_view(), name='user_registration'),
    path('login/', obtain_auth_token, name='user_login'),
    path('logout/', views.UserLogoutAPIView.as_view(), name='user_logout'),
    path('email-verification/',views.PasswordReset.as_view(), name='reset-email'),
    path('password-reset/<str:encoded_pk>/<str:token>/',views.ResetPasswordAPI.as_view(), name='reset-password')
]