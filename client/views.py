from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import ClientSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class ClientView(ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated, )
    http_method_names = ['get', 'post', 'patch', 'put', 'delete']

    def create(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
