from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from main_app.models import User
from main_app.serializers import UserSerializer


class LogInViewSet(viewsets.ViewSet):
    @action(methods=["get"], detail=False)
    def log_in(self, request):
        params = request.query_params
        email = params.get("email", "")
        password = params.get("password", "")

        try:
            user = User.objects.get(email=email, password=password)
            if user.confirmed:
                user.logged_in = True
                user.save()
                return Response(status=200, data={"message": "Log in successful."})
            else:
                return Response(status=422, data={"message": "Please check your email and click the confirmation link "
                                                             "to complete your registration."})
        except User.DoesNotExist:
            return Response(status=422, data={"message": "Incorrect email or password."})


class SignUpViewSet(viewsets.ViewSet):
    @action(methods=["post"], detail=False)
    def create_user(self, request):
        params = request.query_params
        name = params.get("name", "")
        password1 = params.get("password1", "")
        password2 = params.get("password2", "")
        email = params.get("email", "")

        if User.objects.filter(email=email).exists():
            return Response(status=422, data={"message": "Sign up unsuccessful. An account for this email already exists."})

        if password1 != password2:
            return Response(status=422, data={"message": "Sign up unsuccessful. Your passwords must be the same."})

        try:
            validate_password(password1)
            User.objects.create(name=name, password=password1, email=email)
            success_message = "Sign up successful. Please check your email account and click on the confirmation " \
                              "link to access your new account."

            return Response(status=200, data={"message": success_message})
        except ValidationError as e:
            error_message = "Sign up unsuccessful. "

            if hasattr(e, "message_dict"):
                for index, (key, value) in enumerate(e.message_dict.items(), start=1):
                    if index == 1:
                        error_message += "The errors are as follows: "
                    error_message += f"{index}) {key}: {', '.join(value)} "
            else:
                error_message += ", ".join(e.messages)

            return Response(status=422, data={"message": error_message})

    @action(methods=["get"], detail=True)
    def confirm_user(self, request, pk=None):
        from quanda.urls import REACT_MAIN_URL

        user = User.objects.get(id=pk)
        user.confirmed = True
        user.save()
        return HttpResponseRedirect(REACT_MAIN_URL)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
