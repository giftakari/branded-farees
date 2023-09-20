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
from openapi_client.models.form_of_payment_virtual_payment_account import FormOfPaymentVirtualPaymentAccount  # noqa: E501
from openapi_client.rest import ApiException

class TestFormOfPaymentVirtualPaymentAccount(unittest.TestCase):
    """FormOfPaymentVirtualPaymentAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FormOfPaymentVirtualPaymentAccount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FormOfPaymentVirtualPaymentAccount`
        """
        model = openapi_client.models.form_of_payment_virtual_payment_account.FormOfPaymentVirtualPaymentAccount()  # noqa: E501
        if include_optional :
            return FormOfPaymentVirtualPaymentAccount(
                supplier = 'Conferma', 
                account_id = '123', 
                alternate_email_address = [
                    openapi_client.models.email.Email(
                        value = 'exampledomain@example.com', 
                        id = 'exampledomain@example.com', 
                        email_type = 'Work', 
                        comment = '', 
                        preferred_format = 'text/html', 
                        share_marketing = 'Yes', 
                        share_sync = 'Yes', 
                        opt_out_ind = 'Yes', 
                        opt_in_status = 'OptedIn', 
                        opt_in_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        opt_out_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        valid_ind = True, 
                        provisioned_ind = True, )
                    ], 
                payment_comment = '', 
                alternate_hotel_fax = [
                    openapi_client.models.telephone.Telephone(
                        @type = 'Telephone', 
                        country_access_code = '1', 
                        area_city_code = '972', 
                        phone_number = '972-000-787', 
                        extension = '234', 
                        id = '3', 
                        city_code = 'DEN', 
                        role = 'Mobile', )
                    ], 
                maximum_chargeable_amount = [
                    openapi_client.models.currency_amount.CurrencyAmount(
                        value = 124.56, 
                        code = 'USD', 
                        minor_unit = 2, 
                        currency_source = 'Supplier', 
                        approximate_ind = True, )
                    ], 
                incidental_charges = BAR, BUS, CRB
            )
        else :
            return FormOfPaymentVirtualPaymentAccount(
        )
        """

    def testFormOfPaymentVirtualPaymentAccount(self):
        """Test FormOfPaymentVirtualPaymentAccount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()