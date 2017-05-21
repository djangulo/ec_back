import django_filters

from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from .permissions import IsSuperUser

from .models import Press, Publication, Work, WorkPicture
from .support_models import Category, Medium, Program, Status
from . import serializers


class PublicationsByCategory(generics.ListAPIView):
    model = Publication
    serializer_class = serializers.PublicationSerializer
    def get_queryset(self):
        category = Category.publication_items.get(
            slug__iexact=self.kwargs['slug']
        )
        return category.publications.all()


class WorksByCategory(generics.ListAPIView):
    model = Work
    serializer_class = serializers.WorkSerializer
    def get_queryset(self):
        print(self.kwargs)
        category = Category.work_items.get(
            slug__iexact=self.kwargs['slug']
        )
        return category.works.all()


class CategoryViewSet(viewsets.ModelViewSet):
    model = Category
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsSuperUser]


class WorkCategoryViewSet(viewsets.ModelViewSet):
    model = Category
    queryset = Category.work_items.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsSuperUser]


class PublicationCategoryViewSet(viewsets.ModelViewSet):
    model = Category
    queryset = Category.publication_items.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsSuperUser]


class PressLatestViewSet(viewsets.ModelViewSet):
    model = Press
    queryset = Press.objects.order_by('-published_date')[:10]
    serializer_class = serializers.PressSerializer
    permission_classes = [IsSuperUser]


class PressArchiveDatesViewSet(viewsets.ModelViewSet):
    model = Press
    queryset = Press.archive_dates.all()
    serializer_class = serializers.PressDateSerializer
    permission_classes = [IsSuperUser]


class PressByDateViewSet(generics.ListAPIView):
    model = Press
    serializer_class = serializers.PressSerializer
    def get_queryset(self):
        return Press.objects.filter(
            published_date__year=self.kwargs['year']
        ).filter(published_date__month=self.kwargs['month'])


class PressArchiveDatesViewSet(viewsets.ModelViewSet):
    model = Press
    queryset = Press.archive_dates.all()
    serializer_class = serializers.PressDateSerializer
    permission_classes = [IsSuperUser]


class WorksViewSet(viewsets.ModelViewSet):
    model = Work
    queryset = Work.objects.all()
    serializer_class = serializers.WorkSerializer
    permission_classes = [IsSuperUser]


class PublicationsViewSet(viewsets.ModelViewSet):
    model = Publication
    queryset = Publication.objects.all()
    serializer_class = serializers.PublicationSerializer
    permission_classes = [IsSuperUser]


class PressViewSet(viewsets.ModelViewSet):
    model = Press
    queryset = Press.objects.all()
    serializer_class = serializers.PressSerializer
    permissions_classes = [IsSuperUser]
