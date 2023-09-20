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
from openapi_client.models.custom_response_modifiers_air import CustomResponseModifiersAir  # noqa: E501
from openapi_client.rest import ApiException

class TestCustomResponseModifiersAir(unittest.TestCase):
    """CustomResponseModifiersAir unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CustomResponseModifiersAir
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomResponseModifiersAir`
        """
        model = openapi_client.models.custom_response_modifiers_air.CustomResponseModifiersAir()  # noqa: E501
        if include_optional :
            return CustomResponseModifiersAir(
                type = 'CustomResponseModifiersAir', 
                brand_attribute_inclusion = [
                    openapi_client.models.brand_attribute_inclusion.BrandAttributeInclusion(
                        @type = 'BrandAttributeInclusion', 
                        leg_sequence = 1, 
                        classification = [
                            'CheckedBag'
                            ], 
                        additional_classification = [
                            ''
                            ], )
                    ], 
                search_representation = 'Leg', 
                exclude_penalties_ind = True, 
                exclude_baggage_fees_ind = True, 
                include_fare_calculation_ind = True, 
                exclude_surcharges_ind = True, 
                exclude_unbundled_fares_ind = True
            )
        else :
            return CustomResponseModifiersAir(
        )
        """

    def testCustomResponseModifiersAir(self):
        """Test CustomResponseModifiersAir"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
