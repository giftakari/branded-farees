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
from openapi_client.models.traveler_updatable_item_travel_document import TravelerUpdatableItemTravelDocument  # noqa: E501
from openapi_client.rest import ApiException

class TestTravelerUpdatableItemTravelDocument(unittest.TestCase):
    """TravelerUpdatableItemTravelDocument unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TravelerUpdatableItemTravelDocument
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TravelerUpdatableItemTravelDocument`
        """
        model = openapi_client.models.traveler_updatable_item_travel_document.TravelerUpdatableItemTravelDocument()  # noqa: E501
        if include_optional :
            return TravelerUpdatableItemTravelDocument(
                travel_document = openapi_client.models.travel_document.TravelDocument(
                    @type = 'TravelDocumentDetail', 
                    doc_number = 'B37201', 
                    doc_type = 'Passport', 
                    issue_date = 'Sun Oct 13 10:00:00 AEST 2002', 
                    expire_date = 'Wed Nov 13 11:00:00 AEDT 2002', 
                    state_prov_code = '44', 
                    place_of_issue = 'Birmingham', 
                    issue_country = 'CA', 
                    birth_date = 'Sat Apr 22 10:00:00 AEST 1995', 
                    birth_country = 'AR', 
                    birth_place = 'Ontario', 
                    residence = '1st section 8th st', 
                    id = '34', 
                    gender = 'Male', 
                    nationality = 'BR', 
                    person_name = openapi_client.models.person_name.PersonName(
                        @type = 'PersonNameDetail', 
                        prefix = 'Mr', 
                        given = 'John', 
                        middle = 'Erick', 
                        surname = 'Smith', ), )
            )
        else :
            return TravelerUpdatableItemTravelDocument(
        )
        """

    def testTravelerUpdatableItemTravelDocument(self):
        """Test TravelerUpdatableItemTravelDocument"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
