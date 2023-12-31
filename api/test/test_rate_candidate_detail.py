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
from openapi_client.models.rate_candidate_detail import RateCandidateDetail  # noqa: E501
from openapi_client.rest import ApiException

class TestRateCandidateDetail(unittest.TestCase):
    """RateCandidateDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RateCandidateDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RateCandidateDetail`
        """
        model = openapi_client.models.rate_candidate_detail.RateCandidateDetail()  # noqa: E501
        if include_optional :
            return RateCandidateDetail(
                rate_id = 'HL123', 
                customer_loyalty = openapi_client.models.customer_loyalty.CustomerLoyalty(
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
            )
        else :
            return RateCandidateDetail(
        )
        """

    def testRateCandidateDetail(self):
        """Test RateCandidateDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
