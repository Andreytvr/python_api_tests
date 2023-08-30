import pytest
from utils.api_application import ApiApplication
from utils.api_client import ApiClient
from utils.assertions import Assertions
from utils.schemes import Schemes


class TestGetBookingIds:
    name = 'Alexander'
    lastname = "Pushkin"
    checkin = '2023-03-03'
    checkout = '2023-04-04'

    params = [
        f'firstname={name}',
        f'lastname={lastname}',
        f'firstname={name}&lastname={lastname}',
        f'checkout={checkout}'
    ]

    def setup_class(self):
        self.new_booking = ApiApplication.create_booking(self.name, self.lastname, 1000, False, self.checkin,
                                                         self.checkout,
                                                         "Breakfast")
        self.booking_id = self.new_booking.json()['bookingid']

    def test_get_all_booking_ids(self):
        response = ApiClient.get('booking')
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_array_has_more_one_element(response)
        Assertions.assert_jsonschema_validation(response, Schemes.all_booking)

    @pytest.mark.parametrize('param', params)
    def test_get_booking_ids_with_filters(self, param):
        response = ApiClient.get(f"booking?{param}")
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_array_has_value(response, "bookingid", self.booking_id)

    def test_get_booking_by_id(self):
        response = ApiClient.get(f"booking/{self.booking_id}")
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_by_value(response, 'firstname', self.name)
        Assertions.assert_json_by_value(response, 'lastname', self.lastname)
        Assertions.assert_jsonschema_validation(response, Schemes.booking_by_id)
