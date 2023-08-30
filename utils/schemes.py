class Schemes:
    all_booking = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "array",
        "items": [
            {
                "type": "object",
                "properties": {
                    "bookingid": {
                        "type": "integer"
                    }
                },
                "required": [
                    "bookingid"
                ]
            },
            {
                "type": "object",
                "properties": {
                    "bookingid": {
                        "type": "integer"
                    }
                },
                "required": [
                    "bookingid"
                ]
            }
        ]
    }

    booking_by_id = {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "type": "object",
      "properties": {
        "firstname": {
          "type": "string"
        },
        "lastname": {
          "type": "string"
        },
        "totalprice": {
          "type": "integer"
        },
        "depositpaid": {
          "type": "boolean"
        },
        "bookingdates": {
          "type": "object",
          "properties": {
            "checkin": {
              "type": "string"
            },
            "checkout": {
              "type": "string"
            }
          },
          "required": [
            "checkin",
            "checkout"
          ]
        },
        "additionalneeds": {
          "type": "string"
        }
      },
      "required": [
        "firstname",
        "lastname",
        "totalprice",
        "depositpaid",
        "bookingdates",
        "additionalneeds"
      ]
    }
    create_booking = {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "type": "object",
      "properties": {
        "bookingid": {
          "type": "integer"
        },
        "booking": {
          "type": "object",
          "properties": {
            "firstname": {
              "type": "string"
            },
            "lastname": {
              "type": "string"
            },
            "totalprice": {
              "type": "integer"
            },
            "depositpaid": {
              "type": "boolean"
            },
            "bookingdates": {
              "type": "object",
              "properties": {
                "checkin": {
                  "type": "string"
                },
                "checkout": {
                  "type": "string"
                }
              },
              "required": [
                "checkin",
                "checkout"
              ]
            },
            "additionalneeds": {
              "type": "string"
            }
          },
          "required": [
            "firstname",
            "lastname",
            "totalprice",
            "depositpaid",
            "bookingdates",
            "additionalneeds"
          ]
        }
      },
      "required": [
        "bookingid",
        "booking"
      ]
    }

    update_book = {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "type": "object",
      "properties": {
        "firstname": {
          "type": "string"
        },
        "lastname": {
          "type": "string"
        },
        "totalprice": {
          "type": "integer"
        },
        "depositpaid": {
          "type": "boolean"
        },
        "bookingdates": {
          "type": "object",
          "properties": {
            "checkin": {
              "type": "string"
            },
            "checkout": {
              "type": "string"
            }
          },
          "required": [
            "checkin",
            "checkout"
          ]
        },
        "additionalneeds": {
          "type": "string"
        }
      },
      "required": [
        "firstname",
        "lastname",
        "totalprice",
        "depositpaid",
        "bookingdates",
        "additionalneeds"
      ]
    }
