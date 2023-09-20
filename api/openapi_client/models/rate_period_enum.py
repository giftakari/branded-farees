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





class RatePeriodEnum(str, Enum):
    """
    The time period for a rate such as daily, weekly, monthly
    """

    """
    allowed enum values
    """
    HOUR = 'Hour'
    DAY = 'Day'
    WEEK = 'Week'
    MONTH = 'Month'
    YEAR = 'Year'
    TOTAL = 'Total'
    RENTALPERIOD = 'RentalPeriod'
    WEEKEND = 'Weekend'
    BUNDLE = 'Bundle'
    PACKAGE = 'Package'
    EXTRAHOUR = 'ExtraHour'
    EXTRADAY = 'ExtraDay'
    EXTRAWEEK = 'ExtraWeek'
    EXTRAMONTH = 'ExtraMonth'
    OTHER = 'Other'

    @classmethod
    def from_json(cls, json_str: str) -> RatePeriodEnum:
        """Create an instance of RatePeriodEnum from a JSON string"""
        return RatePeriodEnum(json.loads(json_str))

