from utils.api_client import APIClient

api = APIClient()

def test_get_product():
    response = api.get("/products/1")
    assert "id" in response
    assert response["id"] == 1
    assert "title" in response

def test_create_product():
    data = {
        "title": "Producto de prueba",
        "price": 123
    }

    response = api.post("/products/add", data, expected_status=201)
    assert response["title"] == data["title"]
    assert response["price"] == data["price"]

def test_delete_product():
    response = api.delete("/products/1", expected_status=200)
    assert response.status_code == 200
