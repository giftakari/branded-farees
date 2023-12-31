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
from openapi_client.models.telephone_detail import TelephoneDetail  # noqa: E501
from openapi_client.rest import ApiException

class TestTelephoneDetail(unittest.TestCase):
    """TelephoneDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TelephoneDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TelephoneDetail`
        """
        model = openapi_client.models.telephone_detail.TelephoneDetail()  # noqa: E501
        if include_optional :
            return TelephoneDetail(
                phone_location_type = 'Home', 
                phone_tech_type = 'Voice', 
                phone_use_type = 'Home', 
                pin = '3456', 
                priority = 1, 
                privacy = openapi_client.models.privacy.Privacy(
                    id = '2', 
                    share_marketing = 'Yes', 
                    share_sync = 'Yes', 
                    opt_out_ind = 'Yes', 
                    opt_in_status = 'OptedIn', 
                    opt_in_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    opt_out_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                enum_telephone_role = 'Mobile', 
                comment = openapi_client.models.comment.Comment(
                    value = 'Additional comments', 
                    id = 'comment_1', 
                    name = 'Comment name', 
                    language = 'EN', ), 
                default_ind = True, 
                provisioned_ind = False
            )
        else :
            return TelephoneDetail(
        )
        """

    def testTelephoneDetail(self):
        """Test TelephoneDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
