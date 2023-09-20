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
from openapi_client.models.terms_and_conditions_full import TermsAndConditionsFull  # noqa: E501
from openapi_client.rest import ApiException

class TestTermsAndConditionsFull(unittest.TestCase):
    """TermsAndConditionsFull unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TermsAndConditionsFull
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TermsAndConditionsFull`
        """
        model = openapi_client.models.terms_and_conditions_full.TermsAndConditionsFull()  # noqa: E501
        if include_optional :
            return TermsAndConditionsFull(
                expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                customer_loyalty = [
                    openapi_client.models.customer_loyalty.CustomerLoyalty(
                        value = '132456', 
                        id = 'Loyalty_1', 
                        priority = 2, 
                        program_id = 'United', 
                        program_name = 'Mileage Plus', 
                        supplier_type = 'Airline', 
                        supplier = 'UA', 
                        tier = 'Silver', 
                        share_with_supplier = [
                            'LH NH SQ'
                            ], 
                        card_holder_name = 'John Smith', 
                        validated_ind = True, )
                    ], 
                text_block = [
                    openapi_client.models.text_block.TextBlock(
                        @type = 'TextBlockDetail', 
                        title = 'Baggage Details', 
                        id = '2', 
                        text_formatted = [
                            openapi_client.models.text_formatted.TextFormatted(
                                value = 'Formatted text', 
                                language = 'English', 
                                text_format = 'PlainText', )
                            ], )
                    ]
            )
        else :
            return TermsAndConditionsFull(
        )
        """

    def testTermsAndConditionsFull(self):
        """Test TermsAndConditionsFull"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()