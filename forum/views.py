from rest_framework import viewsets
from rest_framework.response import Response


class ForumViewSet(viewsets.ViewSet):
    def list(self, request):
        response = "forum response"
        return Response(response)
