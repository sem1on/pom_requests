import requests

class UpdateObject:
    
    response = None
    response_json = None

    def update_object(self, object_id, payload):

        self.response = requests.patch(
            url=f"https://api.restful-api.dev/objects/{object_id}",
            json=payload
        )
        self.response_json = self.response.json()

    def chek_name(self, name):
        assert self.response_json["name"] == name