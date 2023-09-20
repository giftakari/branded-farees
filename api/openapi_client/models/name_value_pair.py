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

class NameValuePair(BaseModel):
    """
    Used for data stored in Name Value pairs
    """
    value: Optional[constr(strict=True, max_length=512)] = None
    id: Optional[StrictStr] = Field(None, description="Optional internally referenced id")
    name: constr(strict=True, max_length=512) = Field(..., description="Key")
    __properties = ["value", "id", "name"]

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
    def from_json(cls, json_str: str) -> NameValuePair:
        """Create an instance of NameValuePair from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NameValuePair:
        """Create an instance of NameValuePair from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NameValuePair.parse_obj(obj)

        _obj = NameValuePair.parse_obj({
            "value": obj.get("value"),
            "id": obj.get("id"),
            "name": obj.get("name")
        })
        return _obj

