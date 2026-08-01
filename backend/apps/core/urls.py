from django.urls import path

from .views import contact, home


app_name = "core"

urlpatterns = [
    path("", home, name="home"),
    path("contact/", contact, name="contact"),
]