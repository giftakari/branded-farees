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
from openapi_client.models.cancel_penalty import CancelPenalty  # noqa: E501
from openapi_client.rest import ApiException

class TestCancelPenalty(unittest.TestCase):
    """CancelPenalty unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CancelPenalty
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CancelPenalty`
        """
        model = openapi_client.models.cancel_penalty.CancelPenalty()  # noqa: E501
        if include_optional :
            return CancelPenalty(
                type = 'CancelPenalty', 
                deadline = openapi_client.models.deadline.Deadline(
                    @type = 'Deadline', 
                    specific_date = openapi_client.models.date_or_date_windows.DateOrDateWindows(
                        specific = 'Fri Mar 03 11:00:00 AEDT 2023', 
                        start = 'Fri Mar 03 11:00:00 AEDT 2023', 
                        end = 'Fri Mar 03 11:00:00 AEDT 2023', 
                        duration = 'P1D', 
                        duration_unit = 'Minutes', ), 
                    time = '', ), 
                hotel_penalty = openapi_client.models.hotel_penalty.HotelPenalty(
                    @type = '', 
                    subject_to_tax = 'Yes', ), 
                refundable = 'Yes'
            )
        else :
            return CancelPenalty(
        )
        """

    def testCancelPenalty(self):
        """Test CancelPenalty"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
