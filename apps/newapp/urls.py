from django.conf.urls import include, url
from django.urls import path

from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='main-view'),
]
