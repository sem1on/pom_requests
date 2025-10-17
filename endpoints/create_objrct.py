import requests

class CreateObject:

    response = None
    response_json = None

    def new_object(self, payload):
        self.response = requests.post(
            url="https://api.restful-api.dev/objects",
            json=payload
        )
        self.response_json = self.response.json()

    def chek_name(self, name):
        assert self.response_json["name"] == name