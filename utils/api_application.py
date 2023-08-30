import json

from utils.api_client import ApiClient


class ApiApplication:

    @staticmethod
    def get_booking(booking_id: int):
        response = ApiClient.get(f'booking/{booking_id}')
        return response

    @staticmethod
    def create_booking(firstname: str, lastname: str, totalprice: int,
                       depositpaid: bool, checkin: str, checkout: str, additionalneeds: str):
        headers = {"Content-Type": "application/json"}

        data = {
            "firstname": firstname,
            "lastname": lastname,
            "totalprice": totalprice,
            "depositpaid": depositpaid,
            "bookingdates": {
                "checkin": checkin,
                "checkout": checkout
            },
            "additionalneeds": additionalneeds
        }

        response = ApiClient.post("booking", json.dumps(data), headers)
        return response

    @staticmethod
    def update_booking(token: str, booking_id: str, firstname: str, lastname: str, totalprice: int,
                       depositpaid: bool, checkin: str, checkout: str, additionalneeds: str):
        headers = {"Content-Type": "application/json", "Cookie": f"token={token}"}

        data = {
            "firstname": firstname,
            "lastname": lastname,
            "totalprice": totalprice,
            "depositpaid": depositpaid,
            "bookingdates": {
                "checkin": checkin,
                "checkout": checkout
            },
            "additionalneeds": additionalneeds
        }
        response = ApiClient.put(f'booking/{booking_id}', json.dumps(data), headers)
        return response

    @staticmethod
    def create_token(username: str, password: str):
        headers = {"Content-Type": "application/json"}
        data = {
            'username': f'{username}',
            'password': f'{password}'
        }
        response = ApiClient.post('auth', json.dumps(data), headers)
        return response

    @staticmethod
    def partial_update_booking(token: str, booking_id: int, data: dict):
        headers = {"Content-Type": "application/json", "Cookie": f"token={token}"}

        response = ApiClient.patch(f'booking/{booking_id}', json.dumps(data), headers)

        return response

    @staticmethod
    def delete_booking(booking_id: int, token: str):
        headers = {"Content-Type": "application/json", "Cookie": f"token={token}"}
        response = ApiClient.delete(f'booking/{booking_id}', headers=headers)
        return response
