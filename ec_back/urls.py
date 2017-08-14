"""ec_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from accounts.api import UserViewSet, obtain_throttled_auth_token
from publications.api import (
    CategoryViewSet,
    PressViewSet,
    PublicationViewSet,
    StatusViewSet,
    MediumViewSet,
    WorkViewSet,
    WorkPictureViewSet,
)
from accounts.api import UserViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'statuses', StatusViewSet)
router.register(r'mediums', MediumViewSet)
router.register(r'statuses', StatusViewSet)
router.register(r'press', PressViewSet)
router.register(r'publications', PublicationViewSet)
router.register(r'works', WorkViewSet)
router.register(r'users', UserViewSet)
router.register(r'work-pictures', WorkPictureViewSet)

urlpatterns = [
    url(r'^api/v2/auth/', obtain_throttled_auth_token, name='get-token'),
    url(r'^api/v2/', include(router.urls)),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

