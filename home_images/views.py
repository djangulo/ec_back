import os
from django.conf import settings
from django.db.models import Q
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from publications.permissions import IsSuperUser

from .models import HomeImage
from .serializers import HomeImageSerializer


class HomeImageViewSet(viewsets.ModelViewSet):
    model = HomeImage
    queryset = HomeImage.objects.filter(~Q(display_order=0))
    serializer_class = HomeImageSerializer
    permission_classes = [IsSuperUser]

@api_view()
def home_text_api_view(request):
    f = open(os.path.join(settings.BASE_DIR, 'home_text.txt'), 'r+')
    t = f.read()
    f.close()
    return Response({'home-text': t})
