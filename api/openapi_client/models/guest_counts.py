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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from openapi_client.models.guest_count import GuestCount

class GuestCounts(BaseModel):
    """
    GuestCounts
    """
    type: Optional[StrictStr] = Field(None, alias="@type")
    guest_count: conlist(GuestCount, max_items=99, min_items=1) = Field(..., alias="GuestCount")
    __properties = ["@type", "GuestCount"]

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
    def from_json(cls, json_str: str) -> GuestCounts:
        """Create an instance of GuestCounts from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in guest_count (list)
        _items = []
        if self.guest_count:
            for _item in self.guest_count:
                if _item:
                    _items.append(_item.to_dict())
            _dict['GuestCount'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GuestCounts:
        """Create an instance of GuestCounts from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GuestCounts.parse_obj(obj)

        _obj = GuestCounts.parse_obj({
            "type": obj.get("@type"),
            "guest_count": [GuestCount.from_dict(_item) for _item in obj.get("GuestCount")] if obj.get("GuestCount") is not None else None
        })
        return _obj


