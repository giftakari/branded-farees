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
from openapi_client.models.stopover_restriction import StopoverRestriction  # noqa: E501
from openapi_client.rest import ApiException

class TestStopoverRestriction(unittest.TestCase):
    """StopoverRestriction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StopoverRestriction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StopoverRestriction`
        """
        model = openapi_client.models.stopover_restriction.StopoverRestriction()  # noqa: E501
        if include_optional :
            return StopoverRestriction(
                type = 'StopoverRestrictions', 
                stopover_charge_ref = 'Reference1', 
                journey_types = [
                    'OpenJaw'
                    ], 
                departure_carrier = 'XPE', 
                arrival_airline = 'AEH', 
                geographic_restriction = ["Airport","City","Country","StateProvince","Zone"], 
                online_stopover_only_ind = True
            )
        else :
            return StopoverRestriction(
                stopover_charge_ref = 'Reference1',
        )
        """

    def testStopoverRestriction(self):
        """Test StopoverRestriction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()