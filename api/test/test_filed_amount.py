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
from openapi_client.models.filed_amount import FiledAmount  # noqa: E501
from openapi_client.rest import ApiException

class TestFiledAmount(unittest.TestCase):
    """FiledAmount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FiledAmount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FiledAmount`
        """
        model = openapi_client.models.filed_amount.FiledAmount()  # noqa: E501
        if include_optional :
            return FiledAmount(
                value = 43.3422, 
                currency_code = 'USD', 
                code_authority = 'Australian Dollar', 
                decimal_place = 3, 
                decimal_authority = 'ISO 4217'
            )
        else :
            return FiledAmount(
                code_authority = 'Australian Dollar',
                decimal_place = 3,
        )
        """

    def testFiledAmount(self):
        """Test FiledAmount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()