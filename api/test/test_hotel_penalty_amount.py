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
from openapi_client.models.hotel_penalty_amount import HotelPenaltyAmount  # noqa: E501
from openapi_client.rest import ApiException

class TestHotelPenaltyAmount(unittest.TestCase):
    """HotelPenaltyAmount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test HotelPenaltyAmount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HotelPenaltyAmount`
        """
        model = openapi_client.models.hotel_penalty_amount.HotelPenaltyAmount()  # noqa: E501
        if include_optional :
            return HotelPenaltyAmount(
                includes_tax = 'Yes', 
                amount = [
                    openapi_client.models.currency_amount.CurrencyAmount(
                        value = 124.56, 
                        code = 'USD', 
                        minor_unit = 2, 
                        currency_source = 'Supplier', 
                        approximate_ind = True, )
                    ]
            )
        else :
            return HotelPenaltyAmount(
                amount = [
                    openapi_client.models.currency_amount.CurrencyAmount(
                        value = 124.56, 
                        code = 'USD', 
                        minor_unit = 2, 
                        currency_source = 'Supplier', 
                        approximate_ind = True, )
                    ],
        )
        """

    def testHotelPenaltyAmount(self):
        """Test HotelPenaltyAmount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
