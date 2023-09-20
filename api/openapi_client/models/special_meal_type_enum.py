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





class SpecialMealTypeEnum(str, Enum):
    """
    Special Meal Type
    """

    """
    allowed enum values
    """
    BABY = 'Baby'
    BLAND = 'Bland'
    CHILD = 'Child'
    DIABETIC = 'Diabetic'
    FRUITPLATTER = 'FruitPlatter'
    GLUTENINTOLERANT = 'GlutenIntolerant'
    HINDU = 'Hindu'
    JAIN = 'Jain'
    KOSHER = 'Kosher'
    LOWCALORIE = 'LowCalorie'
    LOWFAT = 'LowFat'
    LOWSALT = 'LowSalt'
    MUSLIM = 'Muslim'
    NONLACTOSE = 'NonLactose'
    NONE = 'None'
    SEAFOOD = 'Seafood'
    VEGAN = 'Vegan'
    VEGETARIANHINDU = 'VegetarianHindu'
    VEGETARIANLACTOOVO = 'VegetarianLactoOvo'
    VEGETARIANORIENTAL = 'VegetarianOriental'
    VEGETARIANRAW = 'VegetarianRaw'

    @classmethod
    def from_json(cls, json_str: str) -> SpecialMealTypeEnum:
        """Create an instance of SpecialMealTypeEnum from a JSON string"""
        return SpecialMealTypeEnum(json.loads(json_str))

