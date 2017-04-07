import django_filters

from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from . import models
from . import serializers
from .permissions import IsSuperUser

class PublicationsByCategory(generics.ListCreateAPIView):
    model = models.Publication
    serializer_class = serializers.PublicationSerializer
    def get_queryset(self):
        category = models.Category.objects.get(
            name__iexact=self.kwargs['name']
        )
        return category.publications.all()


class WorksByCategory(generics.ListCreateAPIView):
    model = models.Work
    serializer_class = serializers.WorkSerializer
    def get_queryset(self):
        category = models.Category.objects.get(
            name__iexact=self.kwargs['name']
        )
        return category.works.all()


class WorksList(generics.ListCreateAPIView):
    model = models.Work
    queryset = models.Work.objects.all()
    serializer_class = serializers.WorkSerializer
    permission_classes = [IsSuperUser]

class PublicationsList(generics.ListCreateAPIView):
    model = models.Publication
    queryset = models.Publication.objects.all()
    serializer_class = serializers.PublicationSerializer
    permission_classes = [IsSuperUser]