import django_filters

from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from . import models
from . import serializers

class PublicationsByCategory(generics.ListCreateAPIView):
    model = models.Category
    serializer_class = serializers.CategorySerializer
    def get_queryset(self):
        category = models.Category.objects.get(
            pk=self.kwargs['category_id']
        )
        return category.publication_set.all()


class WorksList(generics.ListCreateAPIView):
    model = models.Work
    queryset = models.Work.objects.all()
    serializer_class = serializers.WorkSerializer