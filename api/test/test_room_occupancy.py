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
from openapi_client.models.room_occupancy import RoomOccupancy  # noqa: E501
from openapi_client.rest import ApiException

class TestRoomOccupancy(unittest.TestCase):
    """RoomOccupancy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RoomOccupancy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoomOccupancy`
        """
        model = openapi_client.models.room_occupancy.RoomOccupancy()  # noqa: E501
        if include_optional :
            return RoomOccupancy(
                type = 'RoomOccupancy', 
                min_occupancy = 0, 
                max_occupancy = 0, 
                age_qualifying = [
                    openapi_client.models.age_qualifying.AgeQualifying(
                        @type = 'AgeQualifying', 
                        min_age = 56, 
                        max_age = 56, 
                        age_bucket = '', 
                        count = 0, 
                        age_qualifying_code = '10', )
                    ]
            )
        else :
            return RoomOccupancy(
        )
        """

    def testRoomOccupancy(self):
        """Test RoomOccupancy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()