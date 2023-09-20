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
from openapi_client.models.refund_options import RefundOptions  # noqa: E501
from openapi_client.rest import ApiException

class TestRefundOptions(unittest.TestCase):
    """RefundOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RefundOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RefundOptions`
        """
        model = openapi_client.models.refund_options.RefundOptions()  # noqa: E501
        if include_optional :
            return RefundOptions(
                type = 'RefundOptions', 
                refund_types = [
                    'Refundable'
                    ], 
                refund_penalty_range = openapi_client.models.refund_penalty_range.RefundPenaltyRange(
                    @type = 'RefundPenaltyRange', 
                    minimum = openapi_client.models.amount_percent.AmountPercent(
                        @type = 'AmountPercentAmount', 
                        application = 'Full', ), 
                    maximum = openapi_client.models.amount_percent.AmountPercent(
                        @type = 'AmountPercentAmount', ), )
            )
        else :
            return RefundOptions(
                refund_types = [
                    'Refundable'
                    ],
        )
        """

    def testRefundOptions(self):
        """Test RefundOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()