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
from openapi_client.models.connection_preferences_air import ConnectionPreferencesAir  # noqa: E501
from openapi_client.rest import ApiException

class TestConnectionPreferencesAir(unittest.TestCase):
    """ConnectionPreferencesAir unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ConnectionPreferencesAir
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConnectionPreferencesAir`
        """
        model = openapi_client.models.connection_preferences_air.ConnectionPreferencesAir()  # noqa: E501
        if include_optional :
            return ConnectionPreferencesAir(
                type = 'ConnectionPreferences', 
                leg_sequence = [
                    56
                    ], 
                max_connection_duration = 'PT3H30M', 
                max_overnight_duration = 'PT6H30M', 
                preference_type = 'Permitted', 
                connection_point = [
                    'AEi012'
                    ], 
                flight_type = openapi_client.models.flight_type.FlightType(
                    @type = 'FlightType', 
                    connection_type = 'StopDirect', 
                    exclude_interline_connections_ind = True, )
            )
        else :
            return ConnectionPreferencesAir(
        )
        """

    def testConnectionPreferencesAir(self):
        """Test ConnectionPreferencesAir"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
