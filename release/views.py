from rest_framework import viewsets
from rest_framework.response import Response


class ReleaseViewSet(viewsets.ViewSet):
    def list(self, request):
        response = "release response"
        return Response(response)
