import json


class IdentityService:

    credentials = {}

    def register(self, username: str, password: str):

        self.credentials = {'username': username, 'password': password}
        return self.credentials

    # def authenticate(username: str, password: str) -> bool:
    #     pass
    #
    def save_to_json(self, path: str):
        with open(path, 'a', encoding='utf-8') as f:
            f.write(json.dumps(self.credentials, indent=3, ensure_ascii=False))



