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
from pydantic import BaseModel, Field, StrictStr, constr

class TextFareRule(BaseModel):
    """
    TextFareRule
    """
    value: Optional[constr(strict=True, max_length=4096)] = None
    language: Optional[StrictStr] = Field(None, description="A three letter code for the representation of names of languages defined by ISO639-3")
    name: Optional[constr(strict=True, max_length=32)] = Field(None, description="The name of the text fare rule")
    __properties = ["value", "language", "name"]

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
    def from_json(cls, json_str: str) -> TextFareRule:
        """Create an instance of TextFareRule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TextFareRule:
        """Create an instance of TextFareRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TextFareRule.parse_obj(obj)

        _obj = TextFareRule.parse_obj({
            "value": obj.get("value"),
            "language": obj.get("language"),
            "name": obj.get("name")
        })
        return _obj


