# coding: utf-8

"""
    Akaris Travels Air

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 11.10.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import Field, StrictStr, constr, validator
from openapi_client.models.day_of_week_enum import DayOfWeekEnum
from openapi_client.models.minimum_stay import MinimumStay

class MinimumStayApplies(MinimumStay):
    """
    MinimumStayApplies
    """
    must_include_day_of_week: Optional[DayOfWeekEnum] = Field(None, alias="mustIncludeDayOfWeek")
    origin_day_of_week: Optional[DayOfWeekEnum] = Field(None, alias="originDayOfWeek")
    return_time: Optional[constr(strict=True)] = Field(None, alias="returnTime", description="Return time")
    duration: StrictStr = Field(..., alias="Duration", description="Minimum duration")
    __properties = ["@type", "mustIncludeDayOfWeek", "originDayOfWeek", "returnTime", "Duration"]

    @validator('return_time')
    def return_time_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"(([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)((:?)[0-5]\d)?([\.,]\d+(?!:))?", value):
            raise ValueError(r"must validate the regular expression /(([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)((:?)[0-5]\d)?([\.,]\d+(?!:))?/")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> MinimumStayApplies:
        """Create an instance of MinimumStayApplies from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MinimumStayApplies:
        """Create an instance of MinimumStayApplies from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MinimumStayApplies.parse_obj(obj)

        _obj = MinimumStayApplies.parse_obj({
            "type": obj.get("@type"),
            "must_include_day_of_week": obj.get("mustIncludeDayOfWeek"),
            "origin_day_of_week": obj.get("originDayOfWeek"),
            "return_time": obj.get("returnTime"),
            "duration": obj.get("Duration")
        })
        return _obj


