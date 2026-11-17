from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("myApp.urls")),
    path("rugby/", include("rugby.urls")),
    path("admin/", admin.site.urls),
]
