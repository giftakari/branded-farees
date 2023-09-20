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





class GenderEnum(str, Enum):
    """
    Gender Type Male, Female etc. This field is not used by Hotel APIs and will be ignored
    """

    """
    allowed enum values
    """
    MALE = 'Male'
    FEMALE = 'Female'
    UNKNOWN = 'Unknown'
    UNDISCLOSED = 'Undisclosed'

    @classmethod
    def from_json(cls, json_str: str) -> GenderEnum:
        """Create an instance of GenderEnum from a JSON string"""
        return GenderEnum(json.loads(json_str))

