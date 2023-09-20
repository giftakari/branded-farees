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
from openapi_client.models.previous_issue import PreviousIssue  # noqa: E501
from openapi_client.rest import ApiException

class TestPreviousIssue(unittest.TestCase):
    """PreviousIssue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PreviousIssue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PreviousIssue`
        """
        model = openapi_client.models.previous_issue.PreviousIssue()  # noqa: E501
        if include_optional :
            return PreviousIssue(
                value = '', 
                issuing_city = 'AEi012', 
                issue_date = '0480-72-88', 
                agency_code_iata = '04807288', 
                document_type = 'Ticket'
            )
        else :
            return PreviousIssue(
        )
        """

    def testPreviousIssue(self):
        """Test PreviousIssue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()