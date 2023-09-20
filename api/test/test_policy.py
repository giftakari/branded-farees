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
from openapi_client.models.policy import Policy  # noqa: E501
from openapi_client.rest import ApiException

class TestPolicy(unittest.TestCase):
    """Policy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Policy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Policy`
        """
        model = openapi_client.models.policy.Policy()  # noqa: E501
        if include_optional :
            return Policy(
                type = 'Policy', 
                title = '', 
                text_formatted = [
                    openapi_client.models.text_formatted.TextFormatted(
                        value = 'Formatted text', 
                        language = 'English', 
                        text_format = 'PlainText', )
                    ], 
                sub_policy = [
                    openapi_client.models.sub_policy.SubPolicy(
                        @type = 'SubPolicy', 
                        title = '', 
                        id = '', 
                        text_formatted = [
                            openapi_client.models.text_formatted.TextFormatted(
                                value = 'Formatted text', 
                                language = 'English', 
                                text_format = 'PlainText', )
                            ], )
                    ]
            )
        else :
            return Policy(
                type = 'Policy',
        )
        """

    def testPolicy(self):
        """Test Policy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
