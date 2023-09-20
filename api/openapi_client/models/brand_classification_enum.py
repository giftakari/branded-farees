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





class BrandClassificationEnum(str, Enum):
    """
    The Travelport classification used for a category of ancillaries such as Seat, Bags, etc. This is an initial list that will be added to.
    """

    """
    allowed enum values
    """
    CHECKEDBAG = 'CheckedBag'
    CARRYON = 'CarryOn'
    PERSONALITEM = 'PersonalItem'
    REBOOKING = 'Rebooking'
    REFUND = 'Refund'
    SEATASSIGNMENT = 'SeatAssignment'
    PREMIUMSEAT = 'PremiumSeat'
    LIEFLATSEAT = 'LieFlatSeat'
    MEALS = 'Meals'
    WIFI = 'WiFi'
    OTHER = 'Other'

    @classmethod
    def from_json(cls, json_str: str) -> BrandClassificationEnum:
        """Create an instance of BrandClassificationEnum from a JSON string"""
        return BrandClassificationEnum(json.loads(json_str))

