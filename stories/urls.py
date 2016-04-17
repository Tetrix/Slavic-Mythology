from django.conf.urls import url, include
from django.views.generic import ListView
from . import views
from home.models import Gods


urlpatterns = [
    # url(r'^$', ListView.as_view(queryset=Gods.objects.all(), template_name="home/gods.html")),
    url(r'^$', views.index, name="index"),
    url(r'^write_a_story/$', views.write_story, name="write_story"),

    ]
