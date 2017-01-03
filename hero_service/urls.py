from django.conf.urls import url

from . import views


app_name = 'hero_service'
urlpatterns = [
    url(r'^hero/$', views.HeroList.as_view(), name='hero_list'),
    url(r'^hero/(?P<pk>\d+)$', views.HeroDetail.as_view(), name='hero_detail'),
]
