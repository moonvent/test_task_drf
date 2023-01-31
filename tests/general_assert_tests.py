from rest_framework import status
from rest_framework.test import APITestCase

from services.constants import CONTENT_TYPE_JSON


def response_result_compare(self: APITestCase, 
                            actual_response,
                            expected_status: int):
    """
        Test result status code and type
    """
    self.assertEqual(actual_response.status_code,
                     expected_status)
    self.assertEqual(actual_response.accepted_media_type,
                     CONTENT_TYPE_JSON)

