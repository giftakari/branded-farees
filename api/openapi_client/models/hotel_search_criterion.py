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
from pydantic import BaseModel, Field, StrictStr, conint, conlist
from openapi_client.models.property_request import PropertyRequest
from openapi_client.models.rate_candidates import RateCandidates
from openapi_client.models.room_stay_candidates import RoomStayCandidates

class HotelSearchCriterion(BaseModel):
    """
    HotelSearchCriterion
    """
    type: Optional[StrictStr] = Field(None, alias="@type")
    number_of_rooms: Optional[conint(strict=True, ge=0)] = Field(None, alias="numberOfRooms", description="Number of rooms requested")
    property_request: conlist(PropertyRequest, max_items=100, min_items=1) = Field(..., alias="PropertyRequest")
    room_stay_candidates: Optional[RoomStayCandidates] = Field(None, alias="RoomStayCandidates")
    rate_candidates: Optional[RateCandidates] = Field(None, alias="RateCandidates")
    __properties = ["@type", "numberOfRooms", "PropertyRequest", "RoomStayCandidates", "RateCandidates"]

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
    def from_json(cls, json_str: str) -> HotelSearchCriterion:
        """Create an instance of HotelSearchCriterion from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in property_request (list)
        _items = []
        if self.property_request:
            for _item in self.property_request:
                if _item:
                    _items.append(_item.to_dict())
            _dict['PropertyRequest'] = _items
        # override the default output from pydantic by calling `to_dict()` of room_stay_candidates
        if self.room_stay_candidates:
            _dict['RoomStayCandidates'] = self.room_stay_candidates.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rate_candidates
        if self.rate_candidates:
            _dict['RateCandidates'] = self.rate_candidates.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HotelSearchCriterion:
        """Create an instance of HotelSearchCriterion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HotelSearchCriterion.parse_obj(obj)

        _obj = HotelSearchCriterion.parse_obj({
            "type": obj.get("@type"),
            "number_of_rooms": obj.get("numberOfRooms"),
            "property_request": [PropertyRequest.from_dict(_item) for _item in obj.get("PropertyRequest")] if obj.get("PropertyRequest") is not None else None,
            "room_stay_candidates": RoomStayCandidates.from_dict(obj.get("RoomStayCandidates")) if obj.get("RoomStayCandidates") is not None else None,
            "rate_candidates": RateCandidates.from_dict(obj.get("RateCandidates")) if obj.get("RateCandidates") is not None else None
        })
        return _obj

