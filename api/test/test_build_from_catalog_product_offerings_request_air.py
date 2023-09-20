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
from openapi_client.models.build_from_catalog_product_offerings_request_air import BuildFromCatalogProductOfferingsRequestAir  # noqa: E501
from openapi_client.rest import ApiException

class TestBuildFromCatalogProductOfferingsRequestAir(unittest.TestCase):
    """BuildFromCatalogProductOfferingsRequestAir unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BuildFromCatalogProductOfferingsRequestAir
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BuildFromCatalogProductOfferingsRequestAir`
        """
        model = openapi_client.models.build_from_catalog_product_offerings_request_air.BuildFromCatalogProductOfferingsRequestAir()  # noqa: E501
        if include_optional :
            return BuildFromCatalogProductOfferingsRequestAir(
                type = 'BuildFromCatalogProductOfferingsRequest', 
                catalog_product_offerings_identifier = openapi_client.models.catalog_product_offerings_identifier.CatalogProductOfferingsIdentifier(
                    id = 'cpo_1', 
                    identifier = openapi_client.models.identifier.Identifier(
                        value = 'A0656EFF-FAF4-456F-B061-0161008D7C4E', 
                        authority = 'TVPT', ), ), 
                catalog_product_offering_selection = [
                    openapi_client.models.catalog_product_offering_selection.CatalogProductOfferingSelection(
                        @type = 'CatalogProductOfferingSelection', 
                        catalog_product_offering_identifier = openapi_client.models.catalog_product_offering_identifier.CatalogProductOfferingIdentifier(
                            id = 'cpo_1', 
                            identifier = openapi_client.models.identifier.Identifier(
                                value = 'A0656EFF-FAF4-456F-B061-0161008D7C4E', 
                                authority = 'TVPT', ), 
                            catalog_product_offering_ref = 'cpo_1', ), 
                        product_brand_offering_identifier = openapi_client.models.identifier.Identifier(
                            value = 'A0656EFF-FAF4-456F-B061-0161008D7C4E', 
                            authority = 'TVPT', ), 
                        product_identifier = [
                            openapi_client.models.product_identifier.ProductIdentifier(
                                id = 'product_1', 
                                product_ref = 'product_1', )
                            ], 
                        segment_sequence = 1, )
                    ], 
                upsell_offering_identifier = [
                    openapi_client.models.upsell_offering_identifier.UpsellOfferingIdentifier(
                        id = '', 
                        identifier = openapi_client.models.identifier.Identifier(
                            value = 'A0656EFF-FAF4-456F-B061-0161008D7C4E', 
                            authority = 'TVPT', ), 
                        catalog_product_offering_ref = '', )
                    ], 
                pricing_modifiers_air = openapi_client.models.pricing_modifiers_air.PricingModifiersAir(
                    @type = 'PricingModifiersAir', 
                    currency_code = 'CAD', 
                    fare_selection = null, 
                    organization_information = openapi_client.models.organization_information.OrganizationInformation(
                        @type = 'OrganizationInformation', 
                        organization_identifier = [
                            openapi_client.models.organization_identifier.OrganizationIdentifier(
                                value = 'JBD123456', 
                                supplier = 'AA', 
                                organization_code_type = 'Account', 
                                segment_sequence_list = [1,2,3], 
                                product_ref = ["product_1","product_2"], 
                                account_code_fares_only_ind = True, )
                            ], 
                        gst_registration_number = [
                            openapi_client.models.gst_registration_number.GSTRegistrationNumber(
                                value = '07AAGFF2194N1Z1', 
                                telephone = '222-222-222', 
                                address = '1122 sample trail, CO, USA, 21232', 
                                country = 'India', 
                                company_name = 'American Airlines', 
                                email = 'sample@aa.com', )
                            ], ), 
                    tax_exemption = openapi_client.models.tax_exemption.TaxExemption(
                        @type = 'TaxExemption', 
                        countries = CA, 
                        tax_codes = ["YQ","US"], 
                        all_taxes_exempt_ind = True, ), 
                    promotional_code = [
                        openapi_client.models.promotional_code.PromotionalCode(
                            value = 'CDFRT', 
                            supplier_code = 'AA', )
                        ], 
                    sell_city = 'MEX', 
                    ticket_city = 'MEX', 
                    pricing_pcc = 'Cu2LC4a01', 
                    ticketing_pcc = 'Cu2LC4a01', 
                    include_split_payment_ind = True, 
                    return_most_restrictive_brand_ind = True, 
                    split_payment_offerings = 25, ), 
                cabin_preference = openapi_client.models.cabin_preference.CabinPreference(
                    @type = 'CabinPreference', 
                    preference_type = 'Preferred', 
                    cabins = [
                        'Economy'
                        ], 
                    leg_sequence = [1,2], ), 
                fare_rule_category = [
                    'AdvanceReservationsTicketing'
                    ], 
                fare_rule_type = 'Structured', 
                custom_response_modifiers_air = openapi_client.models.custom_response_modifiers_air.CustomResponseModifiersAir(
                    @type = 'CustomResponseModifiersAir', 
                    brand_attribute_inclusion = [
                        openapi_client.models.brand_attribute_inclusion.BrandAttributeInclusion(
                            @type = 'BrandAttributeInclusion', 
                            leg_sequence = 1, 
                            classification = [
                                'CheckedBag'
                                ], 
                            additional_classification = [
                                ''
                                ], )
                        ], 
                    search_representation = 'Leg', 
                    exclude_penalties_ind = True, 
                    exclude_baggage_fees_ind = True, 
                    include_fare_calculation_ind = True, 
                    exclude_surcharges_ind = True, 
                    exclude_unbundled_fares_ind = True, ), 
                low_fare_finder_ind = True, 
                re_check_inventory_ind = True, 
                inhibit_brand_content_ind = True, 
                validate_inventory_ind = True
            )
        else :
            return BuildFromCatalogProductOfferingsRequestAir(
                catalog_product_offerings_identifier = openapi_client.models.catalog_product_offerings_identifier.CatalogProductOfferingsIdentifier(
                    id = 'cpo_1', 
                    identifier = openapi_client.models.identifier.Identifier(
                        value = 'A0656EFF-FAF4-456F-B061-0161008D7C4E', 
                        authority = 'TVPT', ), ),
                catalog_product_offering_selection = [
                    openapi_client.models.catalog_product_offering_selection.CatalogProductOfferingSelection(
                        @type = 'CatalogProductOfferingSelection', 
                        catalog_product_offering_identifier = openapi_client.models.catalog_product_offering_identifier.CatalogProductOfferingIdentifier(
                            id = 'cpo_1', 
                            identifier = openapi_client.models.identifier.Identifier(
                                value = 'A0656EFF-FAF4-456F-B061-0161008D7C4E', 
                                authority = 'TVPT', ), 
                            catalog_product_offering_ref = 'cpo_1', ), 
                        product_brand_offering_identifier = openapi_client.models.identifier.Identifier(
                            value = 'A0656EFF-FAF4-456F-B061-0161008D7C4E', 
                            authority = 'TVPT', ), 
                        product_identifier = [
                            openapi_client.models.product_identifier.ProductIdentifier(
                                id = 'product_1', 
                                product_ref = 'product_1', )
                            ], 
                        segment_sequence = 1, )
                    ],
        )
        """

    def testBuildFromCatalogProductOfferingsRequestAir(self):
        """Test BuildFromCatalogProductOfferingsRequestAir"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()