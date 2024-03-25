from app.views import home, form, create
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('form/', form, name="form"),
    path("create/", create, name="create"),
]
