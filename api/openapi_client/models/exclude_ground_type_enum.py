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





class ExcludeGroundTypeEnum(str, Enum):
    """
    ExcludeGroundTypeEnum
    """

    """
    allowed enum values
    """
    TRAIN = 'Train'
    ALL = 'All'

    @classmethod
    def from_json(cls, json_str: str) -> ExcludeGroundTypeEnum:
        """Create an instance of ExcludeGroundTypeEnum from a JSON string"""
        return ExcludeGroundTypeEnum(json.loads(json_str))

