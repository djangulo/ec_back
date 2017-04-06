from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(
        r'^publications/category/(?P<name>[\w\s]+)',
        views.PublicationsByCategory.as_view(),
        name='publications_by_category'
    ),
    url(
        r'^works$',
        views.WorksList.as_view(),
        name='works-list'
    ),
]