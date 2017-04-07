from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(
        r'^$',
        views.UserViewSet.as_view({'get': 'list'}),
        name='staff_list'
    ),
    url(
        r'^(?P<username>[-_.\d\w\s]+)/',
        views.UserViewSet.as_view({'get': 'retrieve'}),
        name='staff_detail'
    ),
]
