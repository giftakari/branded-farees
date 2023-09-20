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
from openapi_client.models.emd import EMD  # noqa: E501
from openapi_client.rest import ApiException

class TestEMD(unittest.TestCase):
    """EMD unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EMD
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EMD`
        """
        model = openapi_client.models.emd.EMD()  # noqa: E501
        if include_optional :
            return EMD(
                person_name = openapi_client.models.person_name.PersonName(
                    @type = 'PersonNameDetail', 
                    prefix = 'Mr', 
                    given = 'John', 
                    middle = 'Erick', 
                    surname = 'Smith', ), 
                reservation_locator = [
                    openapi_client.models.supplier_locator.SupplierLocator(
                        value = 'WTR45G', 
                        supplier_code = 'AA', 
                        supplier_name = 'American Airlines', )
                    ], 
                agency_info = openapi_client.models.agency_info.AgencyInfo(
                    ticketed_date = '2022-04-05', 
                    name = 'Alpha travel', 
                    place = 'Marietta', 
                    ticketing_pcc = '1CR', 
                    code = 'AG1', 
                    sales_type = 'Ticketing', 
                    ticketing_country = 'USA', 
                    ticketing_city = 'Newyork', ), 
                emd_segment = [
                    openapi_client.models.emd_segment.EMDSegment(
                        @type = 'EMDSegment', 
                        sequence = 56, 
                        quantity = 56, 
                        emd_description = openapi_client.models.emd_description.EMDDescription(
                            value = 'meals ticket', 
                            code = 'UPGD', 
                            sub_code = 'wx04we', 
                            code_context = 'ISO', ), 
                        amount = openapi_client.models.amount.Amount(
                            @type = 'Amount', 
                            currency_source = 'Supplier', 
                            currency_code = openapi_client.models.currency_code.CurrencyCode(
                                value = 'USD', 
                                code_authority = 'ISO 4217', 
                                decimal_place = 4, 
                                decimal_authority = 'ISO 4217', ), 
                            base = 120.2, 
                            taxes = openapi_client.models.taxes.Taxes(
                                @type = 'TaxesDetail', 
                                total_taxes = 330.1, 
                                tax_info = [
                                    openapi_client.models.tax_info.TaxInfo(
                                        tax_code = 'XF', 
                                        amount = 1.337, 
                                        tax_breakdown = [
                                            openapi_client.models.tax_breakdown.TaxBreakdown(
                                                airport_code = 'MIA', )
                                            ], )
                                    ], ), 
                            fees = openapi_client.models.fees.Fees(
                                @type = 'FeesDetail', 
                                total_fees = 111.11, ), 
                            total = 30.13, 
                            approximate_ind = True, ), 
                        status = 'Open', 
                        date_of_service = '0480-72-88', 
                        present_to = 'Cu2', 
                        present_at = 'AEi012', 
                        routing = '', )
                    ], 
                total_amount = openapi_client.models.total_amount.TotalAmount(
                    @type = 'Amount', 
                    currency_source = 'Supplier', 
                    currency_code = openapi_client.models.currency_code.CurrencyCode(
                        value = 'USD', 
                        code_authority = 'ISO 4217', 
                        decimal_place = 4, 
                        decimal_authority = 'ISO 4217', ), 
                    base = 120.2, 
                    taxes = openapi_client.models.taxes.Taxes(
                        @type = 'TaxesDetail', 
                        total_taxes = 330.1, 
                        tax_info = [
                            openapi_client.models.tax_info.TaxInfo(
                                tax_code = 'XF', 
                                amount = 1.337, 
                                tax_breakdown = [
                                    openapi_client.models.tax_breakdown.TaxBreakdown(
                                        airport_code = 'MIA', 
                                        amount = 1.337, )
                                    ], )
                            ], ), 
                    fees = openapi_client.models.fees.Fees(
                        @type = 'FeesDetail', 
                        total_fees = 111.11, ), 
                    total = 30.13, 
                    approximate_ind = True, ), 
                form_of_payment = openapi_client.models.form_of_payment.FormOfPayment(
                    value = 'AgencyAccount', 
                    document_number = '45', 
                    encrypted_value = 'BNASJASJKASKJASHJKASK', 
                    document_issuer = 'Alpha travel', 
                    document_type = 'Ticket', ), 
                esac = '', 
                associated_ticket_number = openapi_client.models.ticket_number.TicketNumber(
                    value = '1156', 
                    ticket_issuer = 'Cargo airways', ), 
                restrictions = [
                    ''
                    ]
            )
        else :
            return EMD(
                person_name = openapi_client.models.person_name.PersonName(
                    @type = 'PersonNameDetail', 
                    prefix = 'Mr', 
                    given = 'John', 
                    middle = 'Erick', 
                    surname = 'Smith', ),
                agency_info = openapi_client.models.agency_info.AgencyInfo(
                    ticketed_date = '2022-04-05', 
                    name = 'Alpha travel', 
                    place = 'Marietta', 
                    ticketing_pcc = '1CR', 
                    code = 'AG1', 
                    sales_type = 'Ticketing', 
                    ticketing_country = 'USA', 
                    ticketing_city = 'Newyork', ),
                emd_segment = [
                    openapi_client.models.emd_segment.EMDSegment(
                        @type = 'EMDSegment', 
                        sequence = 56, 
                        quantity = 56, 
                        emd_description = openapi_client.models.emd_description.EMDDescription(
                            value = 'meals ticket', 
                            code = 'UPGD', 
                            sub_code = 'wx04we', 
                            code_context = 'ISO', ), 
                        amount = openapi_client.models.amount.Amount(
                            @type = 'Amount', 
                            currency_source = 'Supplier', 
                            currency_code = openapi_client.models.currency_code.CurrencyCode(
                                value = 'USD', 
                                code_authority = 'ISO 4217', 
                                decimal_place = 4, 
                                decimal_authority = 'ISO 4217', ), 
                            base = 120.2, 
                            taxes = openapi_client.models.taxes.Taxes(
                                @type = 'TaxesDetail', 
                                total_taxes = 330.1, 
                                tax_info = [
                                    openapi_client.models.tax_info.TaxInfo(
                                        tax_code = 'XF', 
                                        amount = 1.337, 
                                        tax_breakdown = [
                                            openapi_client.models.tax_breakdown.TaxBreakdown(
                                                airport_code = 'MIA', )
                                            ], )
                                    ], ), 
                            fees = openapi_client.models.fees.Fees(
                                @type = 'FeesDetail', 
                                total_fees = 111.11, ), 
                            total = 30.13, 
                            approximate_ind = True, ), 
                        status = 'Open', 
                        date_of_service = '0480-72-88', 
                        present_to = 'Cu2', 
                        present_at = 'AEi012', 
                        routing = '', )
                    ],
                form_of_payment = openapi_client.models.form_of_payment.FormOfPayment(
                    value = 'AgencyAccount', 
                    document_number = '45', 
                    encrypted_value = 'BNASJASJKASKJASHJKASK', 
                    document_issuer = 'Alpha travel', 
                    document_type = 'Ticket', ),
        )
        """

    def testEMD(self):
        """Test EMD"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
