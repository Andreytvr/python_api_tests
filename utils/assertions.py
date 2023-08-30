import json

import jsonschema
from requests import Response


class Assertions:
    @staticmethod
    def assert_status_code(response: Response, expected_code):
        assert response.status_code == expected_code, (f'Unexpected status code. Expected code: {expected_code}, '
                                                       f'actual code: {response.status_code}')

    @staticmethod
    def assert_json_array_has_more_one_element(response: Response):
        try:
            response_list = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Response is not json format. Response text = {response.text}'

        assert isinstance(response_list, list)
        assert len(response_list) > 1

    @staticmethod
    def assert_jsonschema_validation(response: Response, schema):
        try:
            response_json = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Response is not json format. Response text = {response.text}'

        jsonschema.validate(response_json, schema)

    @staticmethod
    def assert_json_value(response: Response, name, expected_value):
        try:
            response_json = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Response is not json format. Response text = {response.text}'

        assert response_json[
                   name] == expected_value, f'Expected value: {expected_value}. Current value: {response_json[name]}'

    @staticmethod
    def assert_json_array_has_value(response: Response, name, expected_value):
        try:
            response_json = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Response is not json format. Response text = {response.text}'

        assert isinstance(response_json, list)
        assert list(filter(lambda obj_list: obj_list[name] == expected_value, response_json)), \
            f"Value {expected_value} not found in list. List: {response_json}"

    @staticmethod
    def assert_json_by_value(response: Response, name, expected_value):
        try:
            response_json = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Response is not json format. Response text = {response.text}'

        assert response_json[name] == expected_value, (f'Expected value: {expected_value}. '
                                                       f'Current value: {response_json[name]}')

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_json = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Response is not json format. Response text = {response.text}'

        assert name in response_json, f'Response json no have key {name}'
