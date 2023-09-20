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
from openapi_client.models.product_ancillary_vehicle import ProductAncillaryVehicle  # noqa: E501
from openapi_client.rest import ApiException

class TestProductAncillaryVehicle(unittest.TestCase):
    """ProductAncillaryVehicle unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProductAncillaryVehicle
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductAncillaryVehicle`
        """
        model = openapi_client.models.product_ancillary_vehicle.ProductAncillaryVehicle()  # noqa: E501
        if include_optional :
            return ProductAncillaryVehicle(
                equipment_type_code = openapi_client.models.code.Code(
                    value = 'INS', 
                    code_context = 'infant with a seat', ), 
                free_quantity_included_in_price = 0, 
                max_bookable_quantity = 0
            )
        else :
            return ProductAncillaryVehicle(
        )
        """

    def testProductAncillaryVehicle(self):
        """Test ProductAncillaryVehicle"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()