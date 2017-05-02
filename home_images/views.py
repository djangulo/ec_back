from django.shortcuts import render

from rest_framework import viewsets

from publications.permissions import IsSuperUser

from .models import HomeImage
from . import serializers


class HomeImageViewSet(viewsets.ModelViewSet):
    model = HomeImage
    queryset = HomeImage.objects.all()
    serializer_class = serializers.HomeImageSerializer
    permission_classes = [IsSuperUser]