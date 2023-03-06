import pytest
from app.books.models import Books

@pytest.mark.django_db
def test_books_model():
    book = Books(
        title = "Harry Potter y la Piedra Filosofal",
        genre = "Literatura fantástica",
        year = "1997",
        author = "J.K. Rowling"
    )
    book.save()

    assert book.title == "Harry Potter y la Piedra Filosofal"
    assert book.genre == "Literatura fantástica"
    assert book.year == "1997"
    assert book.author == "J.K. Rowling"
    assert book.created_at
    assert book.updated_at
    assert str(book) == book.title