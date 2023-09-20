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





class TransportationCategoryEnum(str, Enum):
    """
    Transportation Category
    """

    """
    allowed enum values
    """
    BICYCLE = 'Bicycle'
    BOAT = 'Boat'
    BUS = 'Bus'
    CABLECAR = 'CableCar'
    CAR = 'Car'
    CARRIAGE = 'Carriage'
    COURTESY_CAR = 'Courtesy Car'
    HELICOPTER = 'Helicopter'
    LIMOUSINE = 'Limousine'
    METRO = 'Metro'
    MONORAIL = 'Monorail'
    MOTORBIKE = 'Motorbike'
    PACK_ANIMAL = 'Pack Animal'
    PLANE = 'Plane'
    RENTAL_CAR = 'Rental Car'
    RICKSHAW = 'Rickshaw'
    SHUTTLE = 'Shuttle'
    SUBWAY = 'Subway'
    SEDANCHAIR = 'SedanChair'
    TAXI = 'Taxi'
    TRAIN = 'Train'
    TROLLEY = 'Trolley'
    TUBE = 'Tube'
    WALK = 'Walk'
    WATERTAXI = 'WaterTaxi'
    OTHER = 'Other'
    CAR_MINUS_RUSH_HOUR = 'Car-RushHour'
    TAXI_MINUS_RUSH_HOUR = 'Taxi-RushHour'
    EXPRESSTRAIN = 'ExpressTrain'
    PUBLIC = 'Public'
    ALTERNATE = 'Alternate'
    FERRY = 'Ferry'

    @classmethod
    def from_json(cls, json_str: str) -> TransportationCategoryEnum:
        """Create an instance of TransportationCategoryEnum from a JSON string"""
        return TransportationCategoryEnum(json.loads(json_str))

