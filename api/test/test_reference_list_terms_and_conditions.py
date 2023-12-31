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
from openapi_client.models.reference_list_terms_and_conditions import ReferenceListTermsAndConditions  # noqa: E501
from openapi_client.rest import ApiException

class TestReferenceListTermsAndConditions(unittest.TestCase):
    """ReferenceListTermsAndConditions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ReferenceListTermsAndConditions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReferenceListTermsAndConditions`
        """
        model = openapi_client.models.reference_list_terms_and_conditions.ReferenceListTermsAndConditions()  # noqa: E501
        if include_optional :
            return ReferenceListTermsAndConditions(
                terms_and_conditions = [
                    null
                    ]
            )
        else :
            return ReferenceListTermsAndConditions(
        )
        """

    def testReferenceListTermsAndConditions(self):
        """Test ReferenceListTermsAndConditions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
