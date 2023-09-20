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
from openapi_client.models.traveler_list_response_wrapper import TravelerListResponseWrapper  # noqa: E501
from openapi_client.rest import ApiException

class TestTravelerListResponseWrapper(unittest.TestCase):
    """TravelerListResponseWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TravelerListResponseWrapper
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TravelerListResponseWrapper`
        """
        model = openapi_client.models.traveler_list_response_wrapper.TravelerListResponseWrapper()  # noqa: E501
        if include_optional :
            return TravelerListResponseWrapper(
                traveler_list_response = openapi_client.models.traveler_list_response.TravelerListResponse(
                    traveler_id = [
                        openapi_client.models.traveler_id.TravelerID(
                            @type = 'TravelerDetail', 
                            id = '', 
                            traveler_ref = '', 
                            identifier = openapi_client.models.identifier.Identifier(
                                value = 'A0656EFF-FAF4-456F-B061-0161008D7C4E', 
                                authority = 'TVPT', ), )
                        ], )
            )
        else :
            return TravelerListResponseWrapper(
        )
        """

    def testTravelerListResponseWrapper(self):
        """Test TravelerListResponseWrapper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
