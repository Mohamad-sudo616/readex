from django.urls import path

from .views import book_list
from .views import book_list, book_detail

app_name = "books"

urlpatterns = [
    path("", book_list, name="list"),
    path("<slug:slug>/", book_detail, name="detail"),
]