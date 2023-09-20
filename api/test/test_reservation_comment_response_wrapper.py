# coding: utf-8

"""
    Akaris Travels Air

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 11.10.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import openapi_client
from openapi_client.models.reservation_comment_response_wrapper import ReservationCommentResponseWrapper  # noqa: E501
from openapi_client.rest import ApiException

class TestReservationCommentResponseWrapper(unittest.TestCase):
    """ReservationCommentResponseWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ReservationCommentResponseWrapper
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReservationCommentResponseWrapper`
        """
        model = openapi_client.models.reservation_comment_response_wrapper.ReservationCommentResponseWrapper()  # noqa: E501
        if include_optional :
            return ReservationCommentResponseWrapper(
                reservation_comment_response = openapi_client.models.reservation_comment_response.ReservationCommentResponse(
                    reservation_comment = openapi_client.models.reservation_comment_id.ReservationCommentID(
                        @type = 'ReservationComment', 
                        id = '', ), )
            )
        else :
            return ReservationCommentResponseWrapper(
        )
        """

    def testReservationCommentResponseWrapper(self):
        """Test ReservationCommentResponseWrapper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
