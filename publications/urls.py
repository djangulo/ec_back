from django.conf.urls import url, include

from . import views

urlpatterns = [
    # Works URLs
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
        r'^works/categories/$',
        views.WorkCategoryViewSet.as_view({'get': 'list'}),
        name='work-categories'
    ),
    url(
        r'^works/categories/(?P<slug>[-_.\w]+)/',
        views.WorksByCategory.as_view(),
        name='work_by_category'
    ),
    # Publications URLs
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
        r'^publications/categories/$',
        views.PublicationCategoryViewSet.as_view({'get': 'list'}),
        name='publication-categories'
    ),
    url(
        r'^publications/categories/(?P<slug>[-_.\w]+)/',
        views.PublicationsByCategory.as_view(),
        name='pub_by_category'
    ),
    # Press URLs
    url(
        r'^press/$',
        views.PressReleaseViewSet.as_view({'get': 'list'}),
        name='press_release_list'
    ),
    url(
        r'^press/(?P<pk>\d+)/$',
        views.PressReleaseViewSet.as_view({'get': 'retrieve'}),
        name='pub_detail'
    ),
    url(
        r'^press/categories/$',
        views.PressCategoryViewSet.as_view({'get': 'list'}),
        name='press-categories'
    ),
    url(
        r'^categories/$',
        views.CategoryViewSet.as_view({'get': 'list'}),
        name='categories'
    ),
]