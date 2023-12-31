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
from openapi_client.models.catalog_offerings_request_hospitality import CatalogOfferingsRequestHospitality  # noqa: E501
from openapi_client.rest import ApiException

class TestCatalogOfferingsRequestHospitality(unittest.TestCase):
    """CatalogOfferingsRequestHospitality unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CatalogOfferingsRequestHospitality
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CatalogOfferingsRequestHospitality`
        """
        model = openapi_client.models.catalog_offerings_request_hospitality.CatalogOfferingsRequestHospitality()  # noqa: E501
        if include_optional :
            return CatalogOfferingsRequestHospitality(
                type = 'CatalogOfferingsRequestHospitality', 
                search_control_console_channel_id = openapi_client.models.search_control_console_channel_id.SearchControlConsoleChannelID(
                    value = '2', 
                    scc_type = '', ), 
                requested_currency = 'AEi', 
                max_response_wait_time = 56, 
                stay_dates = openapi_client.models.date_or_date_windows.DateOrDateWindows(
                    specific = 'Fri Mar 03 11:00:00 AEDT 2023', 
                    start = 'Fri Mar 03 11:00:00 AEDT 2023', 
                    end = 'Fri Mar 03 11:00:00 AEDT 2023', 
                    duration = 'P1D', 
                    duration_unit = 'Minutes', ), 
                hotel_search_criterion = openapi_client.models.hotel_search_criterion.HotelSearchCriterion(
                    @type = 'HotelSearchCriterion', 
                    number_of_rooms = 0, 
                    property_request = [
                        openapi_client.models.property_request.PropertyRequest(
                            @type = 'PropertyRequest', 
                            more_rates_token = '', 
                            property_key = openapi_client.models.property_key.PropertyKey(
                                @type = 'PropertyKey', 
                                chain_code = 'HL', 
                                property_code = '', ), )
                        ], 
                    room_stay_candidates = openapi_client.models.room_stay_candidates.RoomStayCandidates(
                        room_stay_candidate = [
                            openapi_client.models.room_stay_candidate.RoomStayCandidate(
                                guest_counts = openapi_client.models.guest_counts.GuestCounts(
                                    @type = 'GuestCounts', 
                                    guest_count = [
                                        openapi_client.models.guest_count.GuestCount(
                                            @type = 'GuestCount', 
                                            age = 21, 
                                            count = 2, 
                                            age_qualifying_code = '10', )
                                        ], ), 
                                room_amenity = [
                                    openapi_client.models.room_amenity.RoomAmenity(
                                        @type = 'RoomAmenity', 
                                        description = 'WiFi', 
                                        quantity = 0, 
                                        name = '24 hour Room Service', 
                                        inclusion = [
                                            ''
                                            ], 
                                        included_ind = True, 
                                        surcharge_ind = True, 
                                        code = '8Q6', )
                                    ], )
                            ], ), 
                    rate_candidates = openapi_client.models.rate_candidates.RateCandidates(
                        @type = 'RateCandidates', 
                        rate_candidate = [
                            openapi_client.models.rate_candidate.RateCandidate(
                                @type = 'RateCandidate', 
                                priority = 0, 
                                rate_code = 'HL123', 
                                rate_category = 'All', 
                                chain_code = 'HL', 
                                property_code = 'HL12345', )
                            ], 
                        pre_pay_rates_only_ind = True, 
                        post_pay_rates_only_ind = True, ), ), 
                minimum_amount = openapi_client.models.currency_amount.CurrencyAmount(
                    value = 124.56, 
                    code = 'USD', 
                    minor_unit = 2, 
                    currency_source = 'Supplier', 
                    approximate_ind = True, ), 
                maximum_amount = openapi_client.models.currency_amount.CurrencyAmount(
                    value = 124.56, 
                    code = 'USD', 
                    minor_unit = 2, 
                    currency_source = 'Supplier', 
                    approximate_ind = True, ), 
                verbose_response_ind = True
            )
        else :
            return CatalogOfferingsRequestHospitality(
                stay_dates = openapi_client.models.date_or_date_windows.DateOrDateWindows(
                    specific = 'Fri Mar 03 11:00:00 AEDT 2023', 
                    start = 'Fri Mar 03 11:00:00 AEDT 2023', 
                    end = 'Fri Mar 03 11:00:00 AEDT 2023', 
                    duration = 'P1D', 
                    duration_unit = 'Minutes', ),
        )
        """

    def testCatalogOfferingsRequestHospitality(self):
        """Test CatalogOfferingsRequestHospitality"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
