from django.conf.urls import url, include

from . import views

urlpatterns = [
    # Works URLs
    url(
        r'^works/$',
        views.WorksViewSet.as_view({'get': 'list'}),
        name='work-list'
    ),
    url(
        r'^works/(?P<pk>\d+)/$',
        views.WorksViewSet.as_view({'get': 'retrieve'}),
        name='work-detail'
    ),
    url(
        r'^works/categories/$',
        views.WorkCategoryViewSet.as_view({'get': 'list'}),
        name='work-categories'
    ),
    url(
        r'^works/categories/(?P<slug>[-_.\w]+)/',
        views.WorksByCategory.as_view(),
        name='works-by-category'
    ),
    # Publications URLs
    url(
        r'^publications/$',
        views.PublicationsViewSet.as_view({'get': 'list'}),
        name='publication-list'
    ),
    url(
        r'^publications/(?P<pk>\d+)/$',
        views.PublicationsViewSet.as_view({'get': 'retrieve'}),
        name='publication-detail'
    ),
    url(
        r'^publications/categories/$',
        views.PublicationCategoryViewSet.as_view({'get': 'list'}),
        name='publication-categories'
    ),
    url(
        r'^publications/categories/(?P<slug>[-_.\w]+)/',
        views.PublicationsByCategory.as_view(),
        name='publications-by-category'
    ),
    # Press URLs
    url(
        r'^press/$',
        views.PressViewSet.as_view({'get': 'list'}),
        name='press-list'
    ),
    url(
        r'^press/(?P<pk>\d+)/$',
        views.PressViewSet.as_view({'get': 'retrieve'}),
        name='press-detail'
    ),
    url(
        r'^press/latest/$',
        views.PressLatestViewSet.as_view({'get': 'list'}),
        name='press-latest'
    ),
    url(
        r'^press/archive/$',
        views.PressArchiveDatesViewSet.as_view({'get': 'list'}),
        name='press-archive'
    ),
    url(
        r'^press/archive/(?P<year>\d+)/(?P<month>\d+)/$',
        views.PressByDateViewSet.as_view(),
        name='press-by-date'
    ),
    url(
        r'^categories/$',
        views.CategoryViewSet.as_view({'get': 'list'}),
        name='categories'
    ),
]