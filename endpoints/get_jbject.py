import requests

class GetObject:

    response = None
    response_json = None

    def get_object(self, create_object_id):

        self.response = requests.get(f"https://api.restful-api.dev/objects/{create_object_id}")
        self.response_json = self.response.json()

    def check_id(self, id):
        assert self.response_json["id"] == id