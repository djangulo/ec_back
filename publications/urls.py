from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(
        r'^publications/categories/(?P<slug>[-_.\w]+)/',
        views.PublicationsByCategory.as_view(),
        name='pub_by_category'
    ),
    url(
        r'^works/categories/(?P<slug>[-_.\w]+)/',
        views.WorksByCategory.as_view(),
        name='work_by_category'
    ),
    url(
        r'^works/$',
        views.WorksViewSet.as_view({'get': 'list'}),
        name='work_list'
    ),
    url(
        r'^works/(?P<pk>\d+)/$',
        views.WorksViewSet.as_view({'get': 'retrieve'}),
        name='work_detail'
    ),
    url(
        r'^publications/$',
        views.PublicationsViewSet.as_view({'get': 'list'}),
        name='pub_list'
    ),
    url(
        r'^publications/(?P<pk>\d+)/$',
        views.PublicationsViewSet.as_view({'get': 'retrieve'}),
        name='pub_detail'
    ),
    url(
        r'^press-releases/$',
        views.PressReleaseViewSet.as_view({'get': 'list'}),
        name='press_release_list'
    ),
    url(
        r'^press_release/(?P<pk>\d+)/$',
        views.PublicationsViewSet.as_view({'get': 'retrieve'}),
        name='pub_detail'
    ),
    url(
        r'^categories/$',
        views.CategoryViewSet.as_view({'get': 'list'}),
        name='categories'
    ),
]