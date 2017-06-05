from django.conf.urls import url

from . import views

urlpatterns = [
    # Works URLs
    url(
        r'^images$',
        views.HomeImageViewSet.as_view({'get': 'list'}),
        name='home-images'
    ),
    url(r'^text$',views.home_text_api_view,name='home-text'),
]