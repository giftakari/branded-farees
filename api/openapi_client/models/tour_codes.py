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
from openapi_client.models.tour_code import TourCode
from openapi_client.models.traveler_identifier_ref import TravelerIdentifierRef

class TourCodes(BaseModel):
    """
    TourCodes
    """
    type: Optional[StrictStr] = Field(None, alias="@type")
    traveler_identifier_ref: Optional[conlist(TravelerIdentifierRef, max_items=10)] = Field(None, alias="TravelerIdentifierRef")
    tour_code: TourCode = Field(..., alias="TourCode")
    __properties = ["@type", "TravelerIdentifierRef", "TourCode"]

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
    def from_json(cls, json_str: str) -> TourCodes:
        """Create an instance of TourCodes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in traveler_identifier_ref (list)
        _items = []
        if self.traveler_identifier_ref:
            for _item in self.traveler_identifier_ref:
                if _item:
                    _items.append(_item.to_dict())
            _dict['TravelerIdentifierRef'] = _items
        # override the default output from pydantic by calling `to_dict()` of tour_code
        if self.tour_code:
            _dict['TourCode'] = self.tour_code.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TourCodes:
        """Create an instance of TourCodes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TourCodes.parse_obj(obj)

        _obj = TourCodes.parse_obj({
            "type": obj.get("@type"),
            "traveler_identifier_ref": [TravelerIdentifierRef.from_dict(_item) for _item in obj.get("TravelerIdentifierRef")] if obj.get("TravelerIdentifierRef") is not None else None,
            "tour_code": TourCode.from_dict(obj.get("TourCode")) if obj.get("TourCode") is not None else None
        })
        return _obj

