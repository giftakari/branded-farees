# coding: utf-8

"""
    Akaris Travels Air

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 11.10.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class OrganizationTypeEnum(str, Enum):
    """
    The type of organization such as an Agency, Branch, Company, Supplier, Provider
    """

    """
    allowed enum values
    """
    TRAVELAGENCY = 'TravelAgency'
    AGENCYBRANCH = 'AgencyBranch'
    LOYALTYPROGRAM = 'LoyaltyProgram'
    IDDOCUMENTISSUER = 'IdDocumentIssuer'
    TRAVELSUPPLIER = 'TravelSupplier'
    TRAVELPROVIDER = 'TravelProvider'
    REGULATORY = 'Regulatory'

    @classmethod
    def from_json(cls, json_str: str) -> OrganizationTypeEnum:
        """Create an instance of OrganizationTypeEnum from a JSON string"""
        return OrganizationTypeEnum(json.loads(json_str))


