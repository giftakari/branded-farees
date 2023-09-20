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
from openapi_client.models.offer_response import OfferResponse  # noqa: E501
from openapi_client.rest import ApiException

class TestOfferResponse(unittest.TestCase):
    """OfferResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OfferResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OfferResponse`
        """
        model = openapi_client.models.offer_response.OfferResponse()  # noqa: E501
        if include_optional :
            return OfferResponse(
                offer = openapi_client.models.offer_id.OfferID(
                    @type = 'Offer', 
                    id = 'offer_1', 
                    offer_ref = 'offer_1', 
                    identifier = openapi_client.models.identifier.Identifier(
                        value = 'A0656EFF-FAF4-456F-B061-0161008D7C4E', 
                        authority = 'TVPT', ), ), 
                transaction_id = '', 
                trace_id = '', 
                result = openapi_client.models.result.Result(
                    @type = 'Result', 
                    status = 'Not processed', 
                    error = [
                        openapi_client.models.error.Error(
                            @type = 'Error', 
                            status_code = 56, 
                            message = '', 
                            name_value_pair = [
                                openapi_client.models.name_value_pair.NameValuePair(
                                    value = 'Sunday', 
                                    id = '6', 
                                    name = 'Day1', )
                                ], )
                        ], 
                    warning = [
                        openapi_client.models.warning.Warning(
                            @type = 'Error', 
                            status_code = 56, 
                            message = '', )
                        ], ), 
                identifier = openapi_client.models.identifier.Identifier(
                    value = 'A0656EFF-FAF4-456F-B061-0161008D7C4E', 
                    authority = 'TVPT', ), 
                next_steps = openapi_client.models.next_steps.NextSteps(
                    base_uri = '', 
                    id = '5', 
                    next_step = [
                        openapi_client.models.next_step.NextStep(
                            value = 'www.resourcelocation.com', 
                            id = '2', 
                            action = 'cancel', 
                            method = 'GET', 
                            description = 'remove offer from the order', )
                        ], ), 
                reference_list = [
                    openapi_client.models.reference_list.ReferenceList(
                        @type = 'ReferenceListFlight', 
                        id = '', )
                    ], 
                currency_rate_conversion = [
                    openapi_client.models.currency_rate_conversion.CurrencyRateConversion(
                        @type = 'CurrencyRateConversion', 
                        source_currency = openapi_client.models.currency_code.CurrencyCode(
                            value = 'USD', 
                            code_authority = 'ISO 4217', 
                            decimal_place = 4, 
                            decimal_authority = 'ISO 4217', ), 
                        target_currency = openapi_client.models.currency_code.CurrencyCode(
                            value = 'USD', 
                            code_authority = 'ISO 4217', 
                            decimal_place = 4, 
                            decimal_authority = 'ISO 4217', ), 
                        conversion_rate = openapi_client.models.conversion_rate.ConversionRate(
                            value = 1.337, 
                            rate_authority = 'ISO 4217', 
                            rate_as_of = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), )
                    ]
            )
        else :
            return OfferResponse(
        )
        """

    def testOfferResponse(self):
        """Test OfferResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
