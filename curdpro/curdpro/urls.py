from django.conf.urls import url
from django.contrib import admin
from curdapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^create/', views.insertingdataview),
    url(r'^update/', views.updatingdataview),
    url(r'^delete/', views.deletingdataview),
    url(r'^access/', views.accessdataview),
]
