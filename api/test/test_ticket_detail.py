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
from openapi_client.models.ticket_detail import TicketDetail  # noqa: E501
from openapi_client.rest import ApiException

class TestTicketDetail(unittest.TestCase):
    """TicketDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TicketDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TicketDetail`
        """
        model = openapi_client.models.ticket_detail.TicketDetail()  # noqa: E501
        if include_optional :
            return TicketDetail(
                sell_amount = openapi_client.models.alternate_amount.AlternateAmount(
                    amount = 43.3422, 
                    currency_code = 'USD', 
                    decimal_place = 3, 
                    fare_calculation = 'LON BA SIN R 234.00 BA LON R 234.00NUC468.00END', 
                    rate_of_exchange = 1.234562, ), 
                pricing_pcc = 'Cu2LC4a01'
            )
        else :
            return TicketDetail(
        )
        """

    def testTicketDetail(self):
        """Test TicketDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
