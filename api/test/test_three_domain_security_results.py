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
from openapi_client.models.three_domain_security_results import ThreeDomainSecurityResults  # noqa: E501
from openapi_client.rest import ApiException

class TestThreeDomainSecurityResults(unittest.TestCase):
    """ThreeDomainSecurityResults unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ThreeDomainSecurityResults
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ThreeDomainSecurityResults`
        """
        model = openapi_client.models.three_domain_security_results.ThreeDomainSecurityResults()  # noqa: E501
        if include_optional :
            return ThreeDomainSecurityResults(
                type = 'ThreeDomainSecurityResults', 
                c_avv = 'AAABAFaQRwAAAAAAEZBHAAAAAAA=ECI05', 
                p_a_res_status = '1', 
                signature_verfication = 'Y', 
                transaction_id = '9D920E9-6FCF-4A74-A4E0-D6A591D1108F', 
                x_id = '2bxUs1emK0SCevbivcApzAcAAQk=', 
                e_ci = '2', 
                u_caf_indicator = '0'
            )
        else :
            return ThreeDomainSecurityResults(
        )
        """

    def testThreeDomainSecurityResults(self):
        """Test ThreeDomainSecurityResults"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()