# coding: utf-8

"""
    Akaris Travels Air

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 11.10.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

import openapi_client
from openapi_client.api.fare_rules_api import FareRulesApi  # noqa: E501
from openapi_client.rest import ApiException


class TestFareRulesApi(unittest.TestCase):
    """FareRulesApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.fare_rules_api.FareRulesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_rules_from_catalog_offerings(self):
        """Test case for get_rules_from_catalog_offerings

        Return standalone fare rules with reference to CatalogOfferings  # noqa: E501
        """
        pass

    def test_get_rules_from_catalog_product_offerings(self):
        """Test case for get_rules_from_catalog_product_offerings

        Return standalone fare rules with reference to CatalogProductOfferings  # noqa: E501
        """
        pass

    def test_get_rules_from_offer(self):
        """Test case for get_rules_from_offer

        Return standalone fare rules with reference to an Offer  # noqa: E501
        """
        pass

    def test_get_rules_from_reservation(self):
        """Test case for get_rules_from_reservation

        Return standalone fare rules with reference to a Reservation  # noqa: E501
        """
        pass

    def test_get_rules_from_reservation_workbench(self):
        """Test case for get_rules_from_reservation_workbench

        Return standalone fare rules with reference to a Reservation workbench  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
