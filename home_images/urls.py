from django.conf.urls import url

from . import views

urlpatterns = [
    # Works URLs
    url(
        r'^$',
        views.HomeImageViewSet.as_view({'get': 'list'}),
        name='home-images'
    ),
]