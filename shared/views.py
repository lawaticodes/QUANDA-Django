from django.core.exceptions import ValidationError
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from shared.models import User
from shared.serializers import UserSerializer


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
            return Response(status=422, data={"message": "Sign up unsuccessful. Your passwords must be the same."})

        try:
            User.objects.create(username=username, password=password1, email=email)
            success_message = "Sign up successful. Please confirm your email address to access your new account."
            return Response(status=200, data={"message": success_message})
        except ValidationError as e:
            error_message = "Sign up unsuccessful."

            for index, (key, value) in enumerate(e.message_dict.items(), start=1):
                if index == 1:
                    error_message += " The errors are as follows:"
                error_message += f" {index}) {key}: {', '.join(value)}"

            return Response(status=422, data={"message": error_message})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
