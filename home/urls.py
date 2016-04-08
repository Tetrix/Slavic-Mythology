from django.conf.urls import url, include
from django.views.generic import ListView
from . import views
from home.models import Gods

urlpatterns = [
    url(r'^$', views.index, name="index"),
    # url(r'^gods/$', views.gods, name="gods"),
    url(r'^gods/$', ListView.as_view(queryset=Gods.objects.all(), template_name="home/gods.html")),
    
]
