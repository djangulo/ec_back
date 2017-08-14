from django.core.exceptions import ValidationError
from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import exception_handler

from publications.models import (
    Category,
    Medium,
    Press,
    Publication,
    Status,
    Work,
    WorkPicture
)
from publications.permissions import IsSuperUser
from publications.serializers import (
    CategorySerializer,
    MediumSerializer,
    PressSerializer,
    PublicationSerializer,
    StatusSerializer,
    WorkSerializer,
    WorkPictureSerializer    
)

#V2 API:
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsSuperUser,
    )

    @detail_route(methods=['get'], url_path='works')
    def get_works(self, request, pk=None):
        category = self.get_object()
        works = category.works.all()
        result_page = self.paginate_queryset(works)
        serializer = WorkSerializer(
            result_page, many=True, context={'request': request})
        return self.get_paginated_response(serializer.data)

    @detail_route(methods=['get'], url_path='press')
    def get_presses(self, request, pk=None):
        category = self.get_object()
        presses = category.presses.all()
        result_page = self.paginate_queryset(presses)
        serializer = PressSerializer(
            result_page, many=True, context={'request': request})
        return self.get_paginated_response(serializer.data)

    @detail_route(methods=['get'], url_path='publications')
    def get_publications(self, request, pk=None):
        category = self.get_object()
        publications = category.publications.all()
        result_page = self.paginate_queryset(publications)
        serializer = PublicationSerializer(
            result_page, many=True, context={'request': request})
        return self.get_paginated_response(serializer.data)


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsSuperUser,
    )

    @detail_route(methods=['get'], url_path='works')
    def get_works(self, request, pk=None):
        status = self.get_object()
        works = status.works.all()
        result_page = self.paginate_queryset(works)
        serializer = WorkSerializer(
            result_page, many=True, context={'request': request})
        return self.get_paginated_response(serializer.data)


class MediumViewSet(viewsets.ModelViewSet):
    queryset = Medium.objects.all()
    serializer_class = MediumSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsSuperUser,
    )

    @detail_route(methods=['get'], url_path='publications')
    def get_works(self, request, pk=None):
        medium = self.get_object()
        publications = medium.publications.all()
        result_page = self.paginate_queryset(publications)
        serializer = PublicationSerializer(
            result_page, many=True, context={'request': request})
        return self.get_paginated_response(serializer.data)


class PressViewSet(viewsets.ModelViewSet):
    queryset = Press.objects.all()
    serializer_class = PressSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsSuperUser,
    )


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsSuperUser,
    )


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsSuperUser,
    )

    @detail_route(methods=['get'], url_path='pictures')
    def get_pictures(self, request, pk=None):
        work = self.get_object()
        pictures = work.pictures.all()
        result_page = WorkPictureSerializer(
            result_page, many=True, context={'request': request})
        return self.get_paginated_response(serializer.data)


class WorkPictureViewSet(viewsets.ModelViewSet):
    queryset = WorkPicture.objects.all()
    serializer_class = WorkPictureSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsSuperUser,
    )
