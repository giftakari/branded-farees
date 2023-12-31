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
from openapi_client.models.net_fare_info import NetFareInfo  # noqa: E501
from openapi_client.rest import ApiException

class TestNetFareInfo(unittest.TestCase):
    """NetFareInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NetFareInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NetFareInfo`
        """
        model = openapi_client.models.net_fare_info.NetFareInfo()  # noqa: E501
        if include_optional :
            return NetFareInfo(
                passenger_type_code = 'Cu2LC012', 
                net_fare_breakdown_construction = [
                    openapi_client.models.net_fare_breakdown_construction.NetFareBreakdownConstruction(
                        value = '', 
                        fare_type = '', 
                        rate_of_exchange = 1.337, )
                    ], 
                ticket_base_audit = openapi_client.models.filed_amount.FiledAmount(
                    value = 43.3422, 
                    currency_code = 'USD', 
                    code_authority = 'Australian Dollar', 
                    decimal_place = 3, 
                    decimal_authority = 'ISO 4217', ), 
                ticket_base_passenger = openapi_client.models.ticket_base_passenger.TicketBasePassenger(
                    value = 1.337, 
                    currency_code = 'AEi', 
                    code_authority = '', 
                    decimal_place = 0, 
                    decimal_authority = '', 
                    b_t_ind = True, 
                    i_t_ind = True, )
            )
        else :
            return NetFareInfo(
        )
        """

    def testNetFareInfo(self):
        """Test NetFareInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
