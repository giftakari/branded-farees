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





class NameTypeEnum(str, Enum):
    """
    OTA Code
    """

    """
    allowed enum values
    """
    FORMER = 'Former'
    NICKNAME = 'Nickname'
    ALTERNATE = 'Alternate'
    MAIDEN = 'Maiden'

    @classmethod
    def from_json(cls, json_str: str) -> NameTypeEnum:
        """Create an instance of NameTypeEnum from a JSON string"""
        return NameTypeEnum(json.loads(json_str))


