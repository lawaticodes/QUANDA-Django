from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from shared.models import User


class LogInViewSet(viewsets.ViewSet):
    def list(self, request):
        response = "log in response"
        return Response(response)


class SignUpViewSet(viewsets.ViewSet):
    @action(methods=["post"], detail=False)
    def create_user(self, request):
        params = request.query_params
        username = params.get("username", "")
        password1 = params.get("password1", "")
        password2 = params.get("password2", "")
        email = params.get("email", "")

        if password1 != password2:
            return Response({"status": "fail", "message": "Your passwords must be the same."})

        try:
            user = User.objects.create(username=username, password=password1, email=email)
            user.save()
            status = "success"
            message = "Sign up successful. Please confirm your email address to access your new account."
        except:
            pass
            # catch all validation errors and save relevant message
            status = "fail"
            message = "Did not pass validation. Sign up not successful."

        response = {"status": status, "message": message}
        return Response(response)
