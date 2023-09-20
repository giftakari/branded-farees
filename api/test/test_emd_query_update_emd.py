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
from openapi_client.models.emd_query_update_emd import EMDQueryUpdateEMD  # noqa: E501
from openapi_client.rest import ApiException

class TestEMDQueryUpdateEMD(unittest.TestCase):
    """EMDQueryUpdateEMD unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EMDQueryUpdateEMD
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EMDQueryUpdateEMD`
        """
        model = openapi_client.models.emd_query_update_emd.EMDQueryUpdateEMD()  # noqa: E501
        if include_optional :
            return EMDQueryUpdateEMD(
                type = 'EMDQueryUpdateEMD', 
                agency_code = '04807288', 
                status = '', 
                date_of_issue = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date()
            )
        else :
            return EMDQueryUpdateEMD(
                type = 'EMDQueryUpdateEMD',
                status = '',
        )
        """

    def testEMDQueryUpdateEMD(self):
        """Test EMDQueryUpdateEMD"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
