
from django.contrib import admin
from django.urls import path
from movieportalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('home', views.home),
    path('movieportalapp/output',views.output),
    path('telugu',views.telugu),
    path('movieportalapp/tbook',views.book),
    path('bookconform',views.conform),
]
