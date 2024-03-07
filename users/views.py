from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth import logout
from django.core.mail import EmailMessage
from .models import CustomUser


SUBJECT = "Verify Your Account - Action Required"
HTML_CONTENT = """<p>Dear {0},</p>
<p>
Thank you for choosing Mendo! We are thrilled to have you on board.
To ensure the security of your account and to activate all features, we kindly request you to verify your email address. 
This step is essential in maintaining the integrity of our platform and providing you with a seamless experience.
</p>
<p>
Please follow the link below:
<p>
http://127.0.0.1:5173/account-activation
</p>
<p>
Insert the following activation code: {1}
</p>
<p>
If you did not sign up for Mendo, please ignore this email. 
Your account will remain inactive until you complete the verification process.
</p>
<p>
Thank you for choosing Mendo. We look forward to serving you!
</p>
<p>Best regards,</p>
<p>The Mendo Team</p>
"""
FROM = "juxhinbazelli@gmail.com"


# Create your views here.
class RegisterView(APIView):
    permission_classes = [AllowAny]

    @classmethod
    def post(cls, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        to = serializer.data["email"]
        message = HTML_CONTENT.format(
            serializer.data["name"],
            serializer.data["otp"]

        )

        msg = EmailMessage(SUBJECT, message, FROM, [to])
        msg.content_subtype = "html"
        msg.send()

        return Response({
            "message": "User signed up successfully",
            "result": serializer.data
        })


class ValidateOTPView(APIView):
    permission_classes = [AllowAny]

    @classmethod
    def post(cls, request):
        email = request.data.get("email", "")
        otp = request.data.get("activationCode", "")
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({"email": "User with this email does not exist"}, status.HTTP_404_NOT_FOUND)
        if not user.otp_expired and user.otp == otp:
            user.is_active = True
            user.otp = None
            user.save()
            return Response({"message": "Your account is successfully activated"}, status.HTTP_200_OK)
        if user.is_active:
            return Response({"message": "Bad request"}, status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"activationCode": "Invalid OTP"}, status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    @classmethod
    def post(cls, request):
        logout(request)
        return Response({"message": "Logout successful"})
