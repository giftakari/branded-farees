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
from openapi_client.models.traveler_updatable_item import TravelerUpdatableItem  # noqa: E501
from openapi_client.rest import ApiException

class TestTravelerUpdatableItem(unittest.TestCase):
    """TravelerUpdatableItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TravelerUpdatableItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TravelerUpdatableItem`
        """
        model = openapi_client.models.traveler_updatable_item.TravelerUpdatableItem()  # noqa: E501
        if include_optional :
            return TravelerUpdatableItem(
                type = 'TravelerUpdatableItem', 
                identifier = 'J3754', 
                addable_ind = True, 
                modifiable_ind = True, 
                deletable_ind = True
            )
        else :
            return TravelerUpdatableItem(
                type = 'TravelerUpdatableItem',
        )
        """

    def testTravelerUpdatableItem(self):
        """Test TravelerUpdatableItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()