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
from openapi_client.models.password import Password  # noqa: E501
from openapi_client.rest import ApiException

class TestPassword(unittest.TestCase):
    """Password unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Password
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Password`
        """
        model = openapi_client.models.password.Password()  # noqa: E501
        if include_optional :
            return Password(
                type = 'EncryptionToken', 
                encryption_key = 'secret', 
                encryption_key_method = 'RSA', 
                encryption_method = 'RSA', 
                encrypted_value = '5dfc52b51bd35553df8592078de921bc', 
                mask = 'xxxx436', 
                token = 'A567GTREWQ', 
                token_provider_id = 'c1234532', 
                authentication_method = 'SecurityCode', 
                plain_text = 'un-encrypted data', 
                error_warning = openapi_client.models.error_warning.ErrorWarning(
                    @type = 'Error', 
                    status_code = 56, 
                    message = '', 
                    name_value_pair = [
                        openapi_client.models.name_value_pair.NameValuePair(
                            value = 'Sunday', 
                            id = '6', 
                            name = 'Day1', )
                        ], )
            )
        else :
            return Password(
        )
        """

    def testPassword(self):
        """Test Password"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
