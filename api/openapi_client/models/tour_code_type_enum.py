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





class TourCodeTypeEnum(str, Enum):
    """
    TourCodeTypeEnum
    """

    """
    allowed enum values
    """
    BULK_TOUR = 'Bulk Tour'
    INCLUSIVE_TOUR = 'Inclusive Tour'

    @classmethod
    def from_json(cls, json_str: str) -> TourCodeTypeEnum:
        """Create an instance of TourCodeTypeEnum from a JSON string"""
        return TourCodeTypeEnum(json.loads(json_str))

