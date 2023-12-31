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
from openapi_client.models.brand_text_detail import BrandTextDetail  # noqa: E501
from openapi_client.rest import ApiException

class TestBrandTextDetail(unittest.TestCase):
    """BrandTextDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BrandTextDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BrandTextDetail`
        """
        model = openapi_client.models.brand_text_detail.BrandTextDetail()  # noqa: E501
        if include_optional :
            return BrandTextDetail(
                sequence = 56, 
                description = '', 
                image = openapi_client.models.image.Image(
                    value = '', 
                    dimension_category = '', 
                    width = 42, 
                    height = 43, 
                    caption = 'Ticket', 
                    picture_category = 5, 
                    image_size = 'Large', 
                    picture_of = 'Lobby', ), 
                url = '', 
                date_create_modify = openapi_client.models.date_create_modify.DateCreateModify(
                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    creator_id = 'c1234563', 
                    last_modify = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    last_modifier_id = 'm346789', 
                    purge = 'Sun Jan 01 11:00:00 AEDT 2023', )
            )
        else :
            return BrandTextDetail(
                date_create_modify = openapi_client.models.date_create_modify.DateCreateModify(
                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    creator_id = 'c1234563', 
                    last_modify = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    last_modifier_id = 'm346789', 
                    purge = 'Sun Jan 01 11:00:00 AEDT 2023', ),
        )
        """

    def testBrandTextDetail(self):
        """Test BrandTextDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
