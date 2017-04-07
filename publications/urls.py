from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(
        r'^publications/category/(?P<name>[\w\s]+)/',
        views.PublicationsByCategory.as_view(),
        name='pub_by_category'
    ),
    url(
        r'^works/category/(?P<name>[\w\s]+)/',
        views.WorksByCategory.as_view(),
        name='work_by_category'
    ),
    url(
        r'^works/$',
        views.WorksViewSet.as_view({'get': 'list'}),
        name='works_list'
    ),
    url(
        r'^works/(?P<pk>\d+)/$',
        views.WorksViewSet.as_view({'get': 'retrieve'}),
        name='work_detail'
    ),
]