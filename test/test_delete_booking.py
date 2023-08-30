from setting import config
from utils.api_application import ApiApplication
from utils.assertions import Assertions
from utils.base_case import BaseCase


class TestDeleteBooking(BaseCase):

    def setup_class(self):
        request_get_token = ApiApplication.create_token(config["LOGIN"], config["PASSWORD"])
        self.token = self.get_json_value(request_get_token, "token")

        new_booking = ApiApplication.create_booking('Jon', 'Smith', 1000, False, '2023-09-09', '2023-09-10',
                                                    "Breakfast")
        self.booking_id = new_booking.json()['bookingid']

    def test_delete_booking(self):
        response = ApiApplication.delete_booking(self.booking_id, self.token)
        Assertions.assert_status_code(response, 201)

        deleted_booking = ApiApplication.get_booking(self.booking_id)
        Assertions.assert_status_code(deleted_booking, 404)
