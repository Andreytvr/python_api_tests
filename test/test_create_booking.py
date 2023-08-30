from utils.api_application import ApiApplication
from utils.assertions import Assertions
from utils.schemes import Schemes


class TestCreateBooking:
    name = 'Peter'
    lastname = "Parker"
    checkin = '2023-03-23'
    checkout = '2023-03-24'

    def test_create_booking(self):
        response = ApiApplication.create_booking(self.name, self.lastname, 999, False, self.checkin, self.checkout,
                                                 "Breakfast")
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response, 'bookingid')
        Assertions.assert_jsonschema_validation(response, Schemes.create_booking)
