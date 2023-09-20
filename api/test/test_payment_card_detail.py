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
from openapi_client.models.payment_card_detail import PaymentCardDetail  # noqa: E501
from openapi_client.rest import ApiException

class TestPaymentCardDetail(unittest.TestCase):
    """PaymentCardDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaymentCardDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentCardDetail`
        """
        model = openapi_client.models.payment_card_detail.PaymentCardDetail()  # noqa: E501
        if include_optional :
            return PaymentCardDetail(
                country_of_issue = 'AG', 
                company_card_reference = 'IOR1386861', 
                bank_name = 'Bank of America', 
                bank_country_code = 'BOFAUS3N', 
                bank_state_code = 'NE', 
                card_holder_id = openapi_client.models.identifier.Identifier(
                    value = 'A0656EFF-FAF4-456F-B061-0161008D7C4E', 
                    authority = 'TVPT', ), 
                person_name = openapi_client.models.person_name.PersonName(
                    @type = 'PersonNameDetail', 
                    prefix = 'Mr', 
                    given = 'John', 
                    middle = 'Erick', 
                    surname = 'Smith', ), 
                address = openapi_client.models.address.Address(
                    @type = 'AddressDetail', 
                    id = 'Address_1', 
                    bldg_room = openapi_client.models.address_bldg_room.AddressBldgRoom(
                        value = 'Moore House, Room 101, 23 ABC Street, Windsor, Berkshire, United Kingdom, SL6 51A', 
                        bulding_ind = True, ), 
                    number = openapi_client.models.address_street_number.AddressStreetNumber(
                        value = '23B ABC Street, Windsor, Berkshire, United Kingdom, SL6 51A', 
                        street_nmbr_suffix = 'B', 
                        street_direction = 'NW', 
                        rural_route_nmbr = '76', 
                        po_box = '1001', ), 
                    street = 'ABC Street', 
                    address_line = S Havana,Opposite to USPS, 
                    city = 'Windsor', 
                    county = 'Berkshire', 
                    state_prov = openapi_client.models.state_prov.StateProv(
                        value = 'CA', 
                        name = 'California', ), 
                    country = openapi_client.models.country.Country(
                        value = 'USA', 
                        id = '23', 
                        name = 'United States', 
                        code_context = 'IATA', ), 
                    postal_code = 'Sl6 1AB', 
                    addressee = '', 
                    role = 'Delivery', ), 
                telephone = [
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
                email = [
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
                signature_on_file = openapi_client.models.signature_on_file.SignatureOnFile(
                    @type = 'SignatureOnFile', 
                    date_effective_expire = openapi_client.models.date_effective_expire.DateEffectiveExpire(
                        effective = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        expire = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        expire_date_exclusive_ind = True, ), 
                    signature_on_file_ind = True, ), 
                three_domain_security = openapi_client.models.three_domain_security.ThreeDomainSecurity(
                    @type = 'ThreeDomainSecurity', 
                    three_domain_security_gateway = openapi_client.models.three_domain_security_gateway.ThreeDomainSecurityGateway(
                        @type = 'ThreeDomainSecurityGateway', 
                        e_ci = '2', 
                        merchant_id = 'mycart', 
                        processor_id = '201', 
                        u_rl = 'https://transactionURL', 
                        authentication_verification = openapi_client.models.authentication_verification.AuthenticationVerification(
                            @type = 'EncryptionToken', 
                            encryption_key = 'secret', 
                            encryption_key_method = 'RSA', 
                            encryption_method = 'RSA', 
                            encrypted_value = '5dfc52b51bd35553df8592078de921bc', 
                            mask = 'xxxx436', 
                            token = 'A567GTREWQ', 
                            token_provider_id = 'c1234532', 
                            authentication_method = 'SecurityCode', 
                            plain_text = 'un-encrypted data', 
                            error_warning = openapi_client.models.error_warning.ErrorWarning(
                                @type = 'Error', 
                                status_code = 56, 
                                message = '', 
                                name_value_pair = [
                                    openapi_client.models.name_value_pair.NameValuePair(
                                        value = 'Sunday', 
                                        id = '6', 
                                        name = 'Day1', )
                                    ], ), ), 
                        password = openapi_client.models.password.Password(
                            @type = 'EncryptionToken', 
                            encryption_key = 'secret', 
                            encryption_key_method = 'RSA', 
                            encryption_method = 'RSA', 
                            encrypted_value = '5dfc52b51bd35553df8592078de921bc', 
                            mask = 'xxxx436', 
                            token = 'A567GTREWQ', 
                            token_provider_id = 'c1234532', 
                            plain_text = 'un-encrypted data', ), ), 
                    three_domain_security_results = openapi_client.models.three_domain_security_results.ThreeDomainSecurityResults(
                        @type = 'ThreeDomainSecurityResults', 
                        c_avv = 'AAABAFaQRwAAAAAAEZBHAAAAAAA=ECI05', 
                        p_a_res_status = '1', 
                        signature_verfication = 'Y', 
                        transaction_id = '9D920E9-6FCF-4A74-A4E0-D6A591D1108F', 
                        x_id = '2bxUs1emK0SCevbivcApzAcAAQk=', 
                        e_ci = '2', 
                        u_caf_indicator = '0', ), ), 
                extended_payment_ind = True, 
                enett_ind = True, 
                third_party_ind = True, 
                acceptance_override_ind = True
            )
        else :
            return PaymentCardDetail(
        )
        """

    def testPaymentCardDetail(self):
        """Test PaymentCardDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()