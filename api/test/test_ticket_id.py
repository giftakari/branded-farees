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
from openapi_client.models.ticket_id import TicketID  # noqa: E501
from openapi_client.rest import ApiException

class TestTicketID(unittest.TestCase):
    """TicketID unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TicketID
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TicketID`
        """
        model = openapi_client.models.ticket_id.TicketID()  # noqa: E501
        if include_optional :
            return TicketID(
                type = 'Ticket', 
                obj_id = '', 
                ticket_ref = '', 
                identifier = openapi_client.models.identifier.Identifier(
                    value = 'A0656EFF-FAF4-456F-B061-0161008D7C4E', 
                    authority = 'TVPT', )
            )
        else :
            return TicketID(
                type = 'Ticket',
        )
        """

    def testTicketID(self):
        """Test TicketID"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
