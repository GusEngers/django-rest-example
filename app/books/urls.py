from django.urls import path
from app.books.views import server_testing, BooksList

urlpatterns = [
    path("api/test/", server_testing, name="Server Testing!"),
    path("api/books/", BooksList.as_view())
]