from django.db.models import Q
from django.shortcuts import render

from rest_framework import viewsets

from publications.permissions import IsSuperUser

from . import models
from . import serializers

class UserViewSet(viewsets.ModelViewSet):
    model = models.User
    queryset = models.User.objects.filter(Q(staff_or_intern=1) | Q(staff_or_intern=2))
    serializer_class = serializers.UserSerializer
    permission_classes = [IsSuperUser]
    lookup_field = 'username'
