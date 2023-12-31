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
from openapi_client.models.alternate_contact import AlternateContact  # noqa: E501
from openapi_client.rest import ApiException

class TestAlternateContact(unittest.TestCase):
    """AlternateContact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AlternateContact
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlternateContact`
        """
        model = openapi_client.models.alternate_contact.AlternateContact()  # noqa: E501
        if include_optional :
            return AlternateContact(
                type = 'AlternateContact', 
                id = '', 
                contact_type = 'Relative', 
                relation = 'Mother', 
                person_name = openapi_client.models.person_name.PersonName(
                    @type = 'PersonNameDetail', 
                    prefix = 'Mr', 
                    given = 'John', 
                    middle = 'Erick', 
                    surname = 'Smith', ), 
                address = [
                    openapi_client.models.address.Address(
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
                        role = 'Delivery', )
                    ], 
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
                emergency_ind = True, 
                default_ind = True
            )
        else :
            return AlternateContact(
                person_name = openapi_client.models.person_name.PersonName(
                    @type = 'PersonNameDetail', 
                    prefix = 'Mr', 
                    given = 'John', 
                    middle = 'Erick', 
                    surname = 'Smith', ),
        )
        """

    def testAlternateContact(self):
        """Test AlternateContact"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
