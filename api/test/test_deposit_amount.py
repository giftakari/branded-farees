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
from openapi_client.models.deposit_amount import DepositAmount  # noqa: E501
from openapi_client.rest import ApiException

class TestDepositAmount(unittest.TestCase):
    """DepositAmount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DepositAmount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DepositAmount`
        """
        model = openapi_client.models.deposit_amount.DepositAmount()  # noqa: E501
        if include_optional :
            return DepositAmount(
                currency_amount = openapi_client.models.currency_amount.CurrencyAmount(
                    value = 124.56, 
                    code = 'USD', 
                    minor_unit = 2, 
                    currency_source = 'Supplier', 
                    approximate_ind = True, )
            )
        else :
            return DepositAmount(
                currency_amount = openapi_client.models.currency_amount.CurrencyAmount(
                    value = 124.56, 
                    code = 'USD', 
                    minor_unit = 2, 
                    currency_source = 'Supplier', 
                    approximate_ind = True, ),
        )
        """

    def testDepositAmount(self):
        """Test DepositAmount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
