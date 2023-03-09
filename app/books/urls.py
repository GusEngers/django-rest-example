from django.urls import path
from app.books.views import server_testing, PostAndList, OneDetail

urlpatterns = [
    path("api/test/", server_testing, name="Server Testing!"),
    path("api/books/", PostAndList.as_view()),
    path("api/books/<int:pk>/", OneDetail.as_view())
]