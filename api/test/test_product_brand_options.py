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
from openapi_client.models.product_brand_options import ProductBrandOptions  # noqa: E501
from openapi_client.rest import ApiException

class TestProductBrandOptions(unittest.TestCase):
    """ProductBrandOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProductBrandOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductBrandOptions`
        """
        model = openapi_client.models.product_brand_options.ProductBrandOptions()  # noqa: E501
        if include_optional :
            return ProductBrandOptions(
                type = 'ProductBrandOptions', 
                flight_refs = ["s1","s2","s3"], 
                product_brand_offering = [
                    openapi_client.models.product_brand_offering.ProductBrandOffering(
                        @type = 'ProductBrandOffering', 
                        identifier = openapi_client.models.identifier.Identifier(
                            value = 'A0656EFF-FAF4-456F-B061-0161008D7C4E', 
                            authority = 'TVPT', ), 
                        price = null, 
                        brand = openapi_client.models.brand_id.BrandID(
                            @type = 'BrandID', 
                            id = '', 
                            brand_ref = '', ), 
                        product = [
                            openapi_client.models.product_id.ProductID(
                                @type = 'ProductAir', 
                                id = 'product_1', 
                                product_ref = 'product_1', )
                            ], 
                        terms_and_conditions = openapi_client.models.terms_and_conditions_id.TermsAndConditionsID(
                            @type = 'TermsAndConditionsAir', 
                            id = 'TC_1', 
                            terms_and_conditions_ref = 'TC_1', ), 
                        combinability_code = J1, 
                        best_combinable_price = null, 
                        desirability = 25, 
                        matched_attributes = 7, 
                        brand_status = 'NotOffered', 
                        best_match_ind = True, 
                        co2_emissions_data = openapi_client.models.co2_emissions_data.CO2EmissionsData(
                            @type = '', 
                            actual = openapi_client.models.measurement.Measurement(
                                value = 2.22, 
                                measurement_type = 'Width', 
                                unit = 'Miles', ), 
                            typical = openapi_client.models.measurement.Measurement(
                                value = 2.22, ), 
                            variance = 56, ), )
                    ]
            )
        else :
            return ProductBrandOptions(
                product_brand_offering = [
                    openapi_client.models.product_brand_offering.ProductBrandOffering(
                        @type = 'ProductBrandOffering', 
                        identifier = openapi_client.models.identifier.Identifier(
                            value = 'A0656EFF-FAF4-456F-B061-0161008D7C4E', 
                            authority = 'TVPT', ), 
                        price = null, 
                        brand = openapi_client.models.brand_id.BrandID(
                            @type = 'BrandID', 
                            id = '', 
                            brand_ref = '', ), 
                        product = [
                            openapi_client.models.product_id.ProductID(
                                @type = 'ProductAir', 
                                id = 'product_1', 
                                product_ref = 'product_1', )
                            ], 
                        terms_and_conditions = openapi_client.models.terms_and_conditions_id.TermsAndConditionsID(
                            @type = 'TermsAndConditionsAir', 
                            id = 'TC_1', 
                            terms_and_conditions_ref = 'TC_1', ), 
                        combinability_code = J1, 
                        best_combinable_price = null, 
                        desirability = 25, 
                        matched_attributes = 7, 
                        brand_status = 'NotOffered', 
                        best_match_ind = True, 
                        co2_emissions_data = openapi_client.models.co2_emissions_data.CO2EmissionsData(
                            @type = '', 
                            actual = openapi_client.models.measurement.Measurement(
                                value = 2.22, 
                                measurement_type = 'Width', 
                                unit = 'Miles', ), 
                            typical = openapi_client.models.measurement.Measurement(
                                value = 2.22, ), 
                            variance = 56, ), )
                    ],
        )
        """

    def testProductBrandOptions(self):
        """Test ProductBrandOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
