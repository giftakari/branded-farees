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
from openapi_client.models.traveler_updatable_items_query_build_from_traveler import TravelerUpdatableItemsQueryBuildFromTraveler  # noqa: E501
from openapi_client.rest import ApiException

class TestTravelerUpdatableItemsQueryBuildFromTraveler(unittest.TestCase):
    """TravelerUpdatableItemsQueryBuildFromTraveler unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TravelerUpdatableItemsQueryBuildFromTraveler
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TravelerUpdatableItemsQueryBuildFromTraveler`
        """
        model = openapi_client.models.traveler_updatable_items_query_build_from_traveler.TravelerUpdatableItemsQueryBuildFromTraveler()  # noqa: E501
        if include_optional :
            return TravelerUpdatableItemsQueryBuildFromTraveler(
                type = 'TravelerUpdatableItemsQueryBuildFromTraveler', 
                traveler_identifier = [34,65,23,12,22,81]
            )
        else :
            return TravelerUpdatableItemsQueryBuildFromTraveler(
                type = 'TravelerUpdatableItemsQueryBuildFromTraveler',
        )
        """

    def testTravelerUpdatableItemsQueryBuildFromTraveler(self):
        """Test TravelerUpdatableItemsQueryBuildFromTraveler"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
