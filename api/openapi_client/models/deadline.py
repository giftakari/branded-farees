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
from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.date_or_date_windows import DateOrDateWindows

class Deadline(BaseModel):
    """
    Deadline
    """
    type: Optional[StrictStr] = Field(None, alias="@type")
    specific_date: DateOrDateWindows = Field(..., alias="SpecificDate")
    time: Optional[StrictStr] = Field(None, alias="Time", description="Local time of the property")
    __properties = ["@type", "SpecificDate", "Time"]

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
    def from_json(cls, json_str: str) -> Deadline:
        """Create an instance of Deadline from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of specific_date
        if self.specific_date:
            _dict['SpecificDate'] = self.specific_date.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Deadline:
        """Create an instance of Deadline from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Deadline.parse_obj(obj)

        _obj = Deadline.parse_obj({
            "type": obj.get("@type"),
            "specific_date": DateOrDateWindows.from_dict(obj.get("SpecificDate")) if obj.get("SpecificDate") is not None else None,
            "time": obj.get("Time")
        })
        return _obj


