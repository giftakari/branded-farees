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
from openapi_client.models.validating_airline import ValidatingAirline  # noqa: E501
from openapi_client.rest import ApiException

class TestValidatingAirline(unittest.TestCase):
    """ValidatingAirline unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ValidatingAirline
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ValidatingAirline`
        """
        model = openapi_client.models.validating_airline.ValidatingAirline()  # noqa: E501
        if include_optional :
            return ValidatingAirline(
                type = 'ValidatingAirline', 
                segment_sequence_list = ["segment1","segment2","segment3"], 
                validating_airline = 'QA', 
                product_ref = ["product1","product2","product3"]
            )
        else :
            return ValidatingAirline(
                validating_airline = 'QA',
        )
        """

    def testValidatingAirline(self):
        """Test ValidatingAirline"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
