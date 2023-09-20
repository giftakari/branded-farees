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
from openapi_client.models.address_street_number import AddressStreetNumber  # noqa: E501
from openapi_client.rest import ApiException

class TestAddressStreetNumber(unittest.TestCase):
    """AddressStreetNumber unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AddressStreetNumber
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddressStreetNumber`
        """
        model = openapi_client.models.address_street_number.AddressStreetNumber()  # noqa: E501
        if include_optional :
            return AddressStreetNumber(
                value = '23B ABC Street, Windsor, Berkshire, United Kingdom, SL6 51A', 
                street_nmbr_suffix = 'B', 
                street_direction = 'NW', 
                rural_route_nmbr = '76', 
                po_box = '1001'
            )
        else :
            return AddressStreetNumber(
        )
        """

    def testAddressStreetNumber(self):
        """Test AddressStreetNumber"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
