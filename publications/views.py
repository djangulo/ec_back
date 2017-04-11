import django_filters

from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from .permissions import IsSuperUser

from . import models
from . import serializers


class PublicationsByCategory(generics.ListAPIView):
    model = models.Publication
    serializer_class = serializers.PublicationSerializer
    def get_queryset(self):
        category = models.Category.objects.get(
            slug__iexact=self.kwargs['slug']
        )
        return category.publications.all()


class WorksByCategory(generics.ListAPIView):
    model = models.Work
    serializer_class = serializers.WorkSerializer
    def get_queryset(self):
        print(self.kwargs)
        category = models.Category.objects.get(
            slug__iexact=self.kwargs['slug']
        )
        return category.works.all()


class CategoryViewSet(viewsets.ModelViewSet):
    model = models.Category
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsSuperUser]


class WorksViewSet(viewsets.ModelViewSet):
    model = models.Work
    queryset = models.Work.objects.all()
    serializer_class = serializers.WorkSerializer
    permission_classes = [IsSuperUser]


class PublicationsViewSet(viewsets.ModelViewSet):
    model = models.Publication
    queryset = models.Publication.objects.all()
    serializer_class = serializers.PublicationSerializer
    permission_classes = [IsSuperUser]


class PressReleaseViewSet(viewsets.ModelViewSet):
    model = models.PressRelease
    queryset = models.PressRelease.objects.all()
    serializer_class = serializers.PressReleaseSerializer
    permissions_classes = [IsSuperUser]
