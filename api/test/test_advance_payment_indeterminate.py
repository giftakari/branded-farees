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
from openapi_client.models.advance_payment_indeterminate import AdvancePaymentIndeterminate  # noqa: E501
from openapi_client.rest import ApiException

class TestAdvancePaymentIndeterminate(unittest.TestCase):
    """AdvancePaymentIndeterminate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AdvancePaymentIndeterminate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvancePaymentIndeterminate`
        """
        model = openapi_client.models.advance_payment_indeterminate.AdvancePaymentIndeterminate()  # noqa: E501
        if include_optional :
            return AdvancePaymentIndeterminate(
                indeterminate_ind = True
            )
        else :
            return AdvancePaymentIndeterminate(
        )
        """

    def testAdvancePaymentIndeterminate(self):
        """Test AdvancePaymentIndeterminate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
