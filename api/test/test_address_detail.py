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
from openapi_client.models.address_detail import AddressDetail  # noqa: E501
from openapi_client.rest import ApiException

class TestAddressDetail(unittest.TestCase):
    """AddressDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AddressDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddressDetail`
        """
        model = openapi_client.models.address_detail.AddressDetail()  # noqa: E501
        if include_optional :
            return AddressDetail(
                address_type = 'CLT', 
                use = 'AUT', 
                comment = openapi_client.models.comment.Comment(
                    value = 'Additional comments', 
                    id = 'comment_1', 
                    name = 'Comment name', 
                    language = 'EN', ), 
                privacy = openapi_client.models.privacy.Privacy(
                    id = '2', 
                    share_marketing = 'Yes', 
                    share_sync = 'Yes', 
                    opt_out_ind = 'Yes', 
                    opt_in_status = 'OptedIn', 
                    opt_in_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    opt_out_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                priority = 1, 
                valid_ind = False, 
                provisioned_ind = False
            )
        else :
            return AddressDetail(
        )
        """

    def testAddressDetail(self):
        """Test AddressDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
