from setting import config
from utils.api_application import ApiApplication
from utils.assertions import Assertions
from utils.base_case import BaseCase
from utils.schemes import Schemes


class TestEditBooking(BaseCase):
    name = 'Eddie'
    lastname = "Brock"
    checkin = '2023-03-23'
    checkout = '2023-03-24'

    partial_update_data = {
        'totalprice': 888,
        'additionalneeds': 'bike'
    }

    def setup_class(self):
        request_token = ApiApplication.create_token(config["LOGIN"], config["PASSWORD"])
        self.token = self.get_json_value(request_token, "token")

        new_booking = ApiApplication.create_booking(self.name, self.lastname, 1000, False, self.checkin, self.checkout,
                                                    "Breakfast")
        self.booking_id = new_booking.json()['bookingid']

    def test_update_booking(self):
        response = ApiApplication.update_booking(self.token, self.booking_id, "Venom", "",
                                                 1000, False, self.checkin, self.checkout,
                                                 "Breakfast")

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_by_value(response, "firstname", "Venom")
        Assertions.assert_jsonschema_validation(response, Schemes.update_book)

        updated_booking = ApiApplication.get_booking(self.booking_id)
        Assertions.assert_json_by_value(updated_booking, "firstname", "Venom")

    def test_partial_update_booking(self):
        response = ApiApplication.partial_update_booking(self.token, self.booking_id, self.partial_update_data)
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_by_value(response, 'additionalneeds', 'bike')
        Assertions.assert_json_by_value(response, 'totalprice', 888)

        updated_booking = ApiApplication.get_booking(self.booking_id)
        Assertions.assert_json_by_value(updated_booking, 'additionalneeds', 'bike')
        Assertions.assert_json_by_value(updated_booking, 'totalprice', 888)
