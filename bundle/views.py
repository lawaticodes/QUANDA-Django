from rest_framework import viewsets
from rest_framework.response import Response


class BundleViewSet(viewsets.ViewSet):
    def list(self, request):
        response = "bundle response"
        return Response(response)
