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
from openapi_client.models.penalties import Penalties  # noqa: E501
from openapi_client.rest import ApiException

class TestPenalties(unittest.TestCase):
    """Penalties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Penalties
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Penalties`
        """
        model = openapi_client.models.penalties.Penalties()  # noqa: E501
        if include_optional :
            return Penalties(
                type = 'Penalties', 
                change = [
                    openapi_client.models.change.Change(
                        @type = 'ChangePermitted', 
                        product_refs = ["baloon","food","accesories"], 
                        segment_sequence = [34,56,678,2], )
                    ], 
                cancel = [
                    openapi_client.models.cancel.Cancel(
                        @type = 'CancelPermitted', 
                        product_refs = ["baloon","food","accesories"], 
                        segment_sequence = [34,56,678,2], )
                    ], 
                waiver = [
                    'TicketUpgrade'
                    ], 
                penalty_source_code = openapi_client.models.penalty_source_code.PenaltySourceCode(
                    value = 'Properties of the penalty', 
                    code_context = 'The context of the penalty source', ), 
                passenger_type_codes = ["CHD","UMNR","CNN"], 
                involuntary_ind = True
            )
        else :
            return Penalties(
        )
        """

    def testPenalties(self):
        """Test Penalties"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
