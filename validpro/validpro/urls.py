from django.conf.urls import url
from django.contrib import admin
from validapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.regd_view),
]
