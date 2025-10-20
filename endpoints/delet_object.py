import requests


class DeletObject:

    response = None
    response_json = None

    def delete_object(self, object_id):

        self.response = requests.delete(
            url=f"https://api.restful-api.dev/objects/{object_id}"
        )
        self.response_json= self.response.json()

    def check_status_code_200(self):
        assert self.response.status_code == 200

    def chek_delete_object(self, object_id):
        self.response = requests.get(
            url=f"https://api.restful-api.dev/objects/{object_id}"
        )
        self.response.status_code == 404
