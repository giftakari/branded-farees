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
from openapi_client.models.build_from_products_request_air import BuildFromProductsRequestAir  # noqa: E501
from openapi_client.rest import ApiException

class TestBuildFromProductsRequestAir(unittest.TestCase):
    """BuildFromProductsRequestAir unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BuildFromProductsRequestAir
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BuildFromProductsRequestAir`
        """
        model = openapi_client.models.build_from_products_request_air.BuildFromProductsRequestAir()  # noqa: E501
        if include_optional :
            return BuildFromProductsRequestAir(
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
                passenger_criteria = [
                    openapi_client.models.passenger_criteria.PassengerCriteria(
                        @type = 'PassengerCriteria', 
                        number = 1, 
                        age = 26, 
                        passenger_type_code = 'ADT', 
                        customer_loyalty = [
                            openapi_client.models.customer_loyalty.CustomerLoyalty(
                                value = '132456', 
                                id = 'Loyalty_1', 
                                priority = 2, 
                                program_id = 'United', 
                                program_name = 'Mileage Plus', 
                                supplier_type = 'Airline', 
                                supplier = 'UA', 
                                tier = 'Silver', 
                                share_with_supplier = [
                                    'LH NH SQ'
                                    ], 
                                card_holder_name = 'John Smith', 
                                validated_ind = True, )
                            ], 
                        traveler_geographic_location = openapi_client.models.traveler_geographic_location.TravelerGeographicLocation(
                            value = 'PMI', 
                            traveler_geographic_location_type = 'City', 
                            resident_geographic_code = '', 
                            general_large_family_resident_discount_ind = True, 
                            special_large_family_resident_discount_ind = True, ), 
                        specified_passenger_type_code_only_ind = True, )
                    ], 
                product_criteria_air = [
                    openapi_client.models.product_criteria_air.ProductCriteriaAir(
                        @type = 'ProductCriteriaAir', 
                        sequence = 1, 
                        specific_flight_criteria = [
                            openapi_client.models.specific_flight_criteria.SpecificFlightCriteria(
                                @type = 'SpecificFlightCriteria', 
                                carrier = 'BA', 
                                flight_number = '980', 
                                departure_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                departure_time = '1140', 
                                arrival_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                arrival_time = '1335', 
                                from = 'LHR', 
                                to = 'PAR', 
                                cabin = 'Economy', 
                                class_of_service = 'F', 
                                brand_tier = 2, 
                                segment_sequence = 1, 
                                availability_source_code = 'Z', 
                                content_source = 'GDS', 
                                bound_flights_ind = True, )
                            ], )
                    ], 
                custom_response_modifiers_air = [
                    openapi_client.models.custom_response_modifiers_air.CustomResponseModifiersAir(
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
                        exclude_unbundled_fares_ind = True, )
                    ]
            )
        else :
            return BuildFromProductsRequestAir(
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
                passenger_criteria = [
                    openapi_client.models.passenger_criteria.PassengerCriteria(
                        @type = 'PassengerCriteria', 
                        number = 1, 
                        age = 26, 
                        passenger_type_code = 'ADT', 
                        customer_loyalty = [
                            openapi_client.models.customer_loyalty.CustomerLoyalty(
                                value = '132456', 
                                id = 'Loyalty_1', 
                                priority = 2, 
                                program_id = 'United', 
                                program_name = 'Mileage Plus', 
                                supplier_type = 'Airline', 
                                supplier = 'UA', 
                                tier = 'Silver', 
                                share_with_supplier = [
                                    'LH NH SQ'
                                    ], 
                                card_holder_name = 'John Smith', 
                                validated_ind = True, )
                            ], 
                        traveler_geographic_location = openapi_client.models.traveler_geographic_location.TravelerGeographicLocation(
                            value = 'PMI', 
                            traveler_geographic_location_type = 'City', 
                            resident_geographic_code = '', 
                            general_large_family_resident_discount_ind = True, 
                            special_large_family_resident_discount_ind = True, ), 
                        specified_passenger_type_code_only_ind = True, )
                    ],
                product_criteria_air = [
                    openapi_client.models.product_criteria_air.ProductCriteriaAir(
                        @type = 'ProductCriteriaAir', 
                        sequence = 1, 
                        specific_flight_criteria = [
                            openapi_client.models.specific_flight_criteria.SpecificFlightCriteria(
                                @type = 'SpecificFlightCriteria', 
                                carrier = 'BA', 
                                flight_number = '980', 
                                departure_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                departure_time = '1140', 
                                arrival_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                arrival_time = '1335', 
                                from = 'LHR', 
                                to = 'PAR', 
                                cabin = 'Economy', 
                                class_of_service = 'F', 
                                brand_tier = 2, 
                                segment_sequence = 1, 
                                availability_source_code = 'Z', 
                                content_source = 'GDS', 
                                bound_flights_ind = True, )
                            ], )
                    ],
        )
        """

    def testBuildFromProductsRequestAir(self):
        """Test BuildFromProductsRequestAir"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
