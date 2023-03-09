import pytest
from app.books.models import Books

@pytest.mark.django_db
def test_add_book(client):
    books = Books.objects.all()
    assert len(books) == 0

    response = client.post(
        "/api/books/",
        {
            "title": "El fin de la eternidad",
            "genre": "Ciencia Ficción",
            "author": "Isaac Asimov",
            "year": "1955",
        },
        content_type = "application/json"
    )

    assert response.status_code == 201
    assert response.data["title"] == "El fin de la eternidad"

    books = Books.objects.all()
    assert len(books) == 1

@pytest.mark.django_db
def test_get_single_book(client): # nuevo

    # Given
    libro = Books.objects.create(
        title="El fin de la eternidad",
        genre="Ciencia Ficción",
        author="Isaac Asimov",
        year="1955",
        )

    # When
    resp = client.get(f"/api/libros/{libro.id}/")

    # Then
    assert resp.status_code == 200
    assert resp.data["title"] == "El fin de la eternidad"