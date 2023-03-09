from django.urls import path
from app.books.views import server_testing, BooksList, Algo

urlpatterns = [
    path("api/test/", server_testing, name="Server Testing!"),
    path("api/books/", BooksList.as_view()),
    path("api/books/<int:pk>/", BooksList.as_view())
]