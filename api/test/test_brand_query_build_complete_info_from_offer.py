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
from openapi_client.models.brand_query_build_complete_info_from_offer import BrandQueryBuildCompleteInfoFromOffer  # noqa: E501
from openapi_client.rest import ApiException

class TestBrandQueryBuildCompleteInfoFromOffer(unittest.TestCase):
    """BrandQueryBuildCompleteInfoFromOffer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BrandQueryBuildCompleteInfoFromOffer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BrandQueryBuildCompleteInfoFromOffer`
        """
        model = openapi_client.models.brand_query_build_complete_info_from_offer.BrandQueryBuildCompleteInfoFromOffer()  # noqa: E501
        if include_optional :
            return BrandQueryBuildCompleteInfoFromOffer(
                type = 'BrandQueryBuildCompleteInfoFromOffer', 
                offer_identifier = openapi_client.models.offer_identifier.OfferIdentifier(
                    id = 'offer_1', 
                    offer_ref = 'offer_1', 
                    identifier = openapi_client.models.identifier.Identifier(
                        value = 'A0656EFF-FAF4-456F-B061-0161008D7C4E', 
                        authority = 'TVPT', ), ), 
                product_identifier = [
                    openapi_client.models.product_identifier.ProductIdentifier(
                        id = 'product_1', 
                        product_ref = 'product_1', 
                        identifier = openapi_client.models.identifier.Identifier(
                            value = 'A0656EFF-FAF4-456F-B061-0161008D7C4E', 
                            authority = 'TVPT', ), )
                    ]
            )
        else :
            return BrandQueryBuildCompleteInfoFromOffer(
                type = 'BrandQueryBuildCompleteInfoFromOffer',
                offer_identifier = openapi_client.models.offer_identifier.OfferIdentifier(
                    id = 'offer_1', 
                    offer_ref = 'offer_1', 
                    identifier = openapi_client.models.identifier.Identifier(
                        value = 'A0656EFF-FAF4-456F-B061-0161008D7C4E', 
                        authority = 'TVPT', ), ),
        )
        """

    def testBrandQueryBuildCompleteInfoFromOffer(self):
        """Test BrandQueryBuildCompleteInfoFromOffer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()