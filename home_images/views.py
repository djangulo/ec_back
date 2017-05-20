from django.db.models import Q
from django.shortcuts import render

from rest_framework import viewsets

from publications.permissions import IsSuperUser

from .models import HomeImage
from . import serializers


class HomeImageViewSet(viewsets.ModelViewSet):
    model = HomeImage
    queryset = HomeImage.objects.filter(~Q(display_order=0))
    serializer_class = serializers.HomeImageSerializer
    permission_classes = [IsSuperUser]
