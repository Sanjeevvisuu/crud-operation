from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",get,name="index"),
    path("create/",create,name="create"),
    path("delete/<id>",delete,name="delete"),
    path("update/<id>",update,name="update"),
     
]
