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
from openapi_client.models.accounting_response_wrapper import AccountingResponseWrapper  # noqa: E501
from openapi_client.rest import ApiException

class TestAccountingResponseWrapper(unittest.TestCase):
    """AccountingResponseWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AccountingResponseWrapper
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountingResponseWrapper`
        """
        model = openapi_client.models.accounting_response_wrapper.AccountingResponseWrapper()  # noqa: E501
        if include_optional :
            return AccountingResponseWrapper(
                accounting_response = openapi_client.models.accounting_response.AccountingResponse(
                    accounting = openapi_client.models.accounting_id.AccountingID(
                        @type = 'Accounting', 
                        id = '', 
                        accounting_ref = '', 
                        identifier = openapi_client.models.identifier.Identifier(
                            value = 'A0656EFF-FAF4-456F-B061-0161008D7C4E', 
                            authority = 'TVPT', ), ), )
            )
        else :
            return AccountingResponseWrapper(
        )
        """

    def testAccountingResponseWrapper(self):
        """Test AccountingResponseWrapper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()