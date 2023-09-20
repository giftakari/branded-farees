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
from openapi_client.models.terms_and_conditions_full_hospitality import TermsAndConditionsFullHospitality  # noqa: E501
from openapi_client.rest import ApiException

class TestTermsAndConditionsFullHospitality(unittest.TestCase):
    """TermsAndConditionsFullHospitality unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TermsAndConditionsFullHospitality
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TermsAndConditionsFullHospitality`
        """
        model = openapi_client.models.terms_and_conditions_full_hospitality.TermsAndConditionsFullHospitality()  # noqa: E501
        if include_optional :
            return TermsAndConditionsFullHospitality(
                guarantee = [
                    openapi_client.models.guarantee.Guarantee(
                        @type = 'Guarantee', 
                        code = '', 
                        guarantee_type = 'GuaranteeRequired', 
                        credentials_required_ind = True, )
                    ], 
                cancel_penalty = [
                    openapi_client.models.cancel_penalty.CancelPenalty(
                        @type = 'CancelPenalty', 
                        deadline = openapi_client.models.deadline.Deadline(
                            @type = 'Deadline', 
                            specific_date = openapi_client.models.date_or_date_windows.DateOrDateWindows(
                                specific = 'Fri Mar 03 11:00:00 AEDT 2023', 
                                start = 'Fri Mar 03 11:00:00 AEDT 2023', 
                                end = 'Fri Mar 03 11:00:00 AEDT 2023', 
                                duration = 'P1D', 
                                duration_unit = 'Minutes', ), 
                            time = '', ), 
                        hotel_penalty = openapi_client.models.hotel_penalty.HotelPenalty(
                            @type = '', 
                            subject_to_tax = 'Yes', ), 
                        refundable = 'Yes', )
                    ], 
                accepted_credit_card = [
                    2031 0222 0321 4532
                    ], 
                description = [
                    ''
                    ], 
                meals_included = openapi_client.models.meals_included.MealsIncluded(
                    breakfast_ind = True, 
                    lunch_ind = True, 
                    dinner_ind = True, ), 
                product_rate_code_info = [
                    openapi_client.models.product_rate_code_info.ProductRateCodeInfo(
                        @type = 'ProductRateCodeInfo', 
                        product_ref = 'product_1', 
                        rate_code_info = openapi_client.models.rate_code_info.RateCodeInfo(
                            value = 'Rio', 
                            rate_name = 'Special', 
                            rate_id = '2345', 
                            rate_category = 'All', ), )
                    ], 
                check_in_out_policy = openapi_client.models.check_in_out_policy.CheckInOutPolicy(
                    @type = 'CheckInOutPolicy', 
                    check_in_time = '24:00', 
                    check_out_time = '24:00', 
                    minimum_age = 56, 
                    description = [
                        openapi_client.models.text_title_and_description.TextTitleAndDescription(
                            value = 'Ticket exchanged', 
                            languages = [
                                'English'
                                ], 
                            title = 'Group details.', )
                        ], ), 
                deposit_policy = openapi_client.models.deposit_policy.DepositPolicy(
                    @type = 'DepositPolicy', 
                    deposit = [
                        openapi_client.models.deposit.Deposit(
                            @type = 'DepositAmount', 
                            date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            remainder_ind = True, )
                        ], ), 
                rate_payment_info = 'PrePay'
            )
        else :
            return TermsAndConditionsFullHospitality(
        )
        """

    def testTermsAndConditionsFullHospitality(self):
        """Test TermsAndConditionsFullHospitality"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
