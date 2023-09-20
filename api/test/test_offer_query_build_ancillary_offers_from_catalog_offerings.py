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
from openapi_client.models.offer_query_build_ancillary_offers_from_catalog_offerings import OfferQueryBuildAncillaryOffersFromCatalogOfferings  # noqa: E501
from openapi_client.rest import ApiException

class TestOfferQueryBuildAncillaryOffersFromCatalogOfferings(unittest.TestCase):
    """OfferQueryBuildAncillaryOffersFromCatalogOfferings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OfferQueryBuildAncillaryOffersFromCatalogOfferings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OfferQueryBuildAncillaryOffersFromCatalogOfferings`
        """
        model = openapi_client.models.offer_query_build_ancillary_offers_from_catalog_offerings.OfferQueryBuildAncillaryOffersFromCatalogOfferings()  # noqa: E501
        if include_optional :
            return OfferQueryBuildAncillaryOffersFromCatalogOfferings(
                type = 'OfferQueryBuildAncillaryOffersFromCatalogOfferings', 
                build_ancillary_offers_from_catalog_offerings = [
                    openapi_client.models.build_ancillary_offers_from_catalog_offerings.BuildAncillaryOffersFromCatalogOfferings(
                        @type = 'BuildAncillaryOffersFromCatalogOfferings', 
                        catalog_offerings_identifier = openapi_client.models.catalog_offerings_identifier.CatalogOfferingsIdentifier(
                            id = 'CatalogOfferings_1', 
                            identifier = openapi_client.models.identifier.Identifier(
                                value = 'A0656EFF-FAF4-456F-B061-0161008D7C4E', 
                                authority = 'TVPT', ), ), 
                        catalog_offering_identifier = openapi_client.models.catalog_offering_identifier.CatalogOfferingIdentifier(
                            id = 'co1', 
                            catalog_offering_ref = 'co1', ), 
                        product_identifier = openapi_client.models.product_identifier.ProductIdentifier(
                            id = 'product_1', 
                            product_ref = 'product_1', ), 
                        quantity = 3, 
                        traveler_identifier_ref = openapi_client.models.traveler_identifier_ref.TravelerIdentifierRef(
                            name = '', 
                            passenger_type_code = 'ADT', ), 
                        catalog_offerings_ancillary_list_identifier = openapi_client.models.identifier.Identifier(
                            value = 'A0656EFF-FAF4-456F-B061-0161008D7C4E', 
                            authority = 'TVPT', ), 
                        include_unsellable_ancillaries_ind = True, )
                    ]
            )
        else :
            return OfferQueryBuildAncillaryOffersFromCatalogOfferings(
                type = 'OfferQueryBuildAncillaryOffersFromCatalogOfferings',
                build_ancillary_offers_from_catalog_offerings = [
                    openapi_client.models.build_ancillary_offers_from_catalog_offerings.BuildAncillaryOffersFromCatalogOfferings(
                        @type = 'BuildAncillaryOffersFromCatalogOfferings', 
                        catalog_offerings_identifier = openapi_client.models.catalog_offerings_identifier.CatalogOfferingsIdentifier(
                            id = 'CatalogOfferings_1', 
                            identifier = openapi_client.models.identifier.Identifier(
                                value = 'A0656EFF-FAF4-456F-B061-0161008D7C4E', 
                                authority = 'TVPT', ), ), 
                        catalog_offering_identifier = openapi_client.models.catalog_offering_identifier.CatalogOfferingIdentifier(
                            id = 'co1', 
                            catalog_offering_ref = 'co1', ), 
                        product_identifier = openapi_client.models.product_identifier.ProductIdentifier(
                            id = 'product_1', 
                            product_ref = 'product_1', ), 
                        quantity = 3, 
                        traveler_identifier_ref = openapi_client.models.traveler_identifier_ref.TravelerIdentifierRef(
                            name = '', 
                            passenger_type_code = 'ADT', ), 
                        catalog_offerings_ancillary_list_identifier = openapi_client.models.identifier.Identifier(
                            value = 'A0656EFF-FAF4-456F-B061-0161008D7C4E', 
                            authority = 'TVPT', ), 
                        include_unsellable_ancillaries_ind = True, )
                    ],
        )
        """

    def testOfferQueryBuildAncillaryOffersFromCatalogOfferings(self):
        """Test OfferQueryBuildAncillaryOffersFromCatalogOfferings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
