from rest_framework import viewsets
from rest_framework.response import Response


class LogInViewSet(viewsets.ViewSet):
    def list(self, request):
        response = "log in response"
        return Response(response)


class SignUpViewSet(viewsets.ViewSet):
    def list(self, request):
        response = "sign up response"
        return Response(response)
