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
from openapi_client.models.additional_brand_attribute import AdditionalBrandAttribute  # noqa: E501
from openapi_client.rest import ApiException

class TestAdditionalBrandAttribute(unittest.TestCase):
    """AdditionalBrandAttribute unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AdditionalBrandAttribute
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdditionalBrandAttribute`
        """
        model = openapi_client.models.additional_brand_attribute.AdditionalBrandAttribute()  # noqa: E501
        if include_optional :
            return AdditionalBrandAttribute(
                type = 'AdditionalBrandAttribute', 
                classification = '', 
                inclusion = 'Included', 
                image_url = [
                    ''
                    ], 
                matched_attribute_ind = True, 
                group_code = 'BG', 
                sub_group_code = 'CY', 
                sub_code = '08A'
            )
        else :
            return AdditionalBrandAttribute(
                type = 'AdditionalBrandAttribute',
                classification = '',
                inclusion = 'Included',
        )
        """

    def testAdditionalBrandAttribute(self):
        """Test AdditionalBrandAttribute"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()