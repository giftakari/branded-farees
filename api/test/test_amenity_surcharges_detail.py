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
from openapi_client.models.amenity_surcharges_detail import AmenitySurchargesDetail  # noqa: E501
from openapi_client.rest import ApiException

class TestAmenitySurchargesDetail(unittest.TestCase):
    """AmenitySurchargesDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AmenitySurchargesDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AmenitySurchargesDetail`
        """
        model = openapi_client.models.amenity_surcharges_detail.AmenitySurchargesDetail()  # noqa: E501
        if include_optional :
            return AmenitySurchargesDetail(
                surcharge = [
                    openapi_client.models.surcharge.Surcharge(
                        value = 12, 
                        currency_code = 'USD', 
                        surcharge_code = 'ADDITIONAL COSTS', 
                        reporting_authority = 'Federal register', 
                        purpose = 'tax for extra service', 
                        description = 'Additional data', 
                        surcharge_application = 'PerPerson', 
                        surcharge_frequency = 'PerNight', 
                        code_authority = 'ISO 4217', 
                        decimal_place = 4, 
                        decimal_authority = 'ISO 4217', )
                    ]
            )
        else :
            return AmenitySurchargesDetail(
                surcharge = [
                    openapi_client.models.surcharge.Surcharge(
                        value = 12, 
                        currency_code = 'USD', 
                        surcharge_code = 'ADDITIONAL COSTS', 
                        reporting_authority = 'Federal register', 
                        purpose = 'tax for extra service', 
                        description = 'Additional data', 
                        surcharge_application = 'PerPerson', 
                        surcharge_frequency = 'PerNight', 
                        code_authority = 'ISO 4217', 
                        decimal_place = 4, 
                        decimal_authority = 'ISO 4217', )
                    ],
        )
        """

    def testAmenitySurchargesDetail(self):
        """Test AmenitySurchargesDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
