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





class MeasurementTypeEnum(str, Enum):
    """
    The type of measurement such as width, height, weight
    """

    """
    allowed enum values
    """
    WIDTH = 'Width'
    HEIGHT = 'Height'
    DEPTH = 'Depth'
    WEIGHT = 'Weight'
    OVERALLDIMENSION = 'OverallDimension'

    @classmethod
    def from_json(cls, json_str: str) -> MeasurementTypeEnum:
        """Create an instance of MeasurementTypeEnum from a JSON string"""
        return MeasurementTypeEnum(json.loads(json_str))


