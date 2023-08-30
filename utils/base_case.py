import json

from requests import Response


class BaseCase:
    @staticmethod
    def get_json_value(response: Response, name):
        try:
            response_json = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Response is not json format. Response text = {response.text}'
        assert name in response_json, f'Key {name} no have in json'
        return response_json[name]
