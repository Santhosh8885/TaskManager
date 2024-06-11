from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import logout
from rest_framework import generics, permissions
from .serializers import UserSerializer,EmailSerializer,ResetPasswordSerializer
from rest_framework import permissions
from rest_framework import generics, status, viewsets, response
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail



class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

class UserLogoutAPIView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'message': 'Logged out successfully'})
    


class PasswordReset(generics.GenericAPIView):
    """
    Request for Password Reset Link.
    """

    serializer_class = EmailSerializer
    permission_classes = (permissions.AllowAny,)


    def post(self, request):
        """
        Create token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data["email"]
        user = User.objects.filter(email=email).first()
        if user:
            encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)
            reset_url = reverse(
                "reset-password",
                kwargs={"encoded_pk": encoded_pk, "token": token},
            )
            reset_link = f"http://127.0.0.1:8000{reset_url}"

            # send the rest_link as mail to the user.
            send_mail(
                'Password Reset Request',
                f'Your password reset link: {reset_link}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

            return response.Response(
                {
                    "message": 
                    f"Your password rest link: {reset_link}"
                },
                status=status.HTTP_200_OK,
            )
        else:
            return response.Response(
                {"message": "User doesn't exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ResetPasswordAPI(generics.GenericAPIView):
    """
    Verify and Reset Password Token View.
    """

    serializer_class = ResetPasswordSerializer
    permission_classes = (permissions.AllowAny,)


    def patch(self, request, *args, **kwargs):
        """
        Verify token & encoded_pk and then reset the password.
        """
        serializer = self.serializer_class(
            data=request.data, context={"kwargs": kwargs}
        )
        serializer.is_valid(raise_exception=True)
        return response.Response(
            {"message": "Password reset complete"},
            status=status.HTTP_200_OK,
        )