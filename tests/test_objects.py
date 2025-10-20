import requests
import pytest

from endpoints.create_objrct import CreateObject
from endpoints.get_jbject import GetObject
from endpoints.update_object import UpdateObject
from endpoints.delet_object import DeletObject

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
    new_object_endpiont = CreateObject()
    payload = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
                }
            }
    new_object_endpiont.new_object(payload=payload)
    new_object_endpiont.check_status_code_200()
    new_object_endpiont.chek_name(payload["name"])



def test_get_object(create_object_id):
    get_object_by_id = GetObject()
    get_object_by_id.get_object(create_object_id)
    get_object_by_id.check_idcreate_object_id()


def test_update_object(create_object_id):
    update_object = UpdateObject()
    payload = {
            "name": "Apple MacBook Pro 21",
            "data": {
                "year": 2025,
                "price": 2149.99,
                "CPU model": "M4",
                "Hard disk size": "1 TB"
                }
            }
    update_object.update_object(create_object_id, payload)
    update_object.chek_name(payload["name"])


def test_delete_object(create_object_id):
    delet_object_endpoint = DeletObject()
    delet_object_endpoint.delete_object(create_object_id)
    delet_object_endpoint.check_status_code_200()
    delet_object_endpoint.chek_delete_object(create_object_id)



