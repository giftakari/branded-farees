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

from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field, constr

class DateCreateModify(BaseModel):
    """
    Time stamp of the creation.
    """
    value: Optional[datetime] = None
    creator_id: Optional[constr(strict=True, max_length=32)] = Field(None, alias="creatorID", description="ID of creator. Software system identifier or an employee id")
    last_modify: Optional[datetime] = Field(None, alias="lastModify", description="Time stamp of last modification.")
    last_modifier_id: Optional[constr(strict=True, max_length=32)] = Field(None, alias="lastModifierID", description="Identifies the last software system or person to modify a record")
    purge: Optional[date] = Field(None, description="Date an item will be purged from a system of record")
    __properties = ["value", "creatorID", "lastModify", "lastModifierID", "purge"]

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
    def from_json(cls, json_str: str) -> DateCreateModify:
        """Create an instance of DateCreateModify from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DateCreateModify:
        """Create an instance of DateCreateModify from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DateCreateModify.parse_obj(obj)

        _obj = DateCreateModify.parse_obj({
            "value": obj.get("value"),
            "creator_id": obj.get("creatorID"),
            "last_modify": obj.get("lastModify"),
            "last_modifier_id": obj.get("lastModifierID"),
            "purge": obj.get("purge")
        })
        return _obj


