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





class RateQualifierEnum(str, Enum):
    """
    A closed enumeration of possible rate qualifiers for vehicle rental
    """

    """
    allowed enum values
    """
    OTHER = 'Other'
    POSTPAYMENT = 'PostPayment'
    GUARANTEE = 'Guarantee'
    PREPAYMENT = 'PrePayment'
    DEPOSIT = 'Deposit'

    @classmethod
    def from_json(cls, json_str: str) -> RateQualifierEnum:
        """Create an instance of RateQualifierEnum from a JSON string"""
        return RateQualifierEnum(json.loads(json_str))


