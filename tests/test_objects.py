import requests
import pytest


@pytest.fixture()
def create_object_id():
    payload = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
                }
            }
    response = requests.post(
        url="https://api.restful-api.dev/objects",
        json=payload
    )
    obj_id = response.json()["id"]
    yield obj_id
    requests.delete(f"https://api.restful-api.dev/objects/{obj_id}")


def test_create_obj(): 
    payload = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
                }
            }
    response = requests.post(
        url="https://api.restful-api.dev/objects",
        json=payload
    )
    assert response.json()["name"] == payload["name"]



def test_get_object(create_object_id):
    response = requests.get(f"https://api.restful-api.dev/objects/{create_object_id}").json()
    assert create_object_id == response["id"]


def test_update_object(create_object_id):
    payload = {
            "name": "Apple MacBook Pro 21",
            "data": {
                "year": 2025,
                "price": 2149.99,
                "CPU model": "M4",
                "Hard disk size": "1 TB"
                }
            }
    response = requests.patch(
        url=f"https://api.restful-api.dev/objects/{create_object_id}",
        json=payload
    )
    assert payload["name"] == response.json()["name"]


def test_delete_object(create_object_id):
    response = requests.delete(
        url=f"https://api.restful-api.dev/objects/{create_object_id}"
    )
    assert response.status_code == 200
    response = requests.get(f"https://api.restful-api.dev/objects/{create_object_id}")
    assert response.status_code == 404



