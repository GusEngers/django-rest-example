import json
from django.urls import reverse

def test_book(client):
    url = reverse("Server Testing!")
    response = client.get(url)
    data = json.loads(response.content)

    assert response.status_code == 200
    assert data["status"] == "Servidor funcionando!!"
