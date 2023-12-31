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
from openapi_client.models.date_range import DateRange  # noqa: E501
from openapi_client.rest import ApiException

class TestDateRange(unittest.TestCase):
    """DateRange unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DateRange
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DateRange`
        """
        model = openapi_client.models.date_range.DateRange()  # noqa: E501
        if include_optional :
            return DateRange(
                start = 'Fri Mar 03 11:00:00 AEDT 2023', 
                end = 'Fri Mar 03 11:00:00 AEDT 2023'
            )
        else :
            return DateRange(
                start = 'Fri Mar 03 11:00:00 AEDT 2023',
                end = 'Fri Mar 03 11:00:00 AEDT 2023',
        )
        """

    def testDateRange(self):
        """Test DateRange"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
