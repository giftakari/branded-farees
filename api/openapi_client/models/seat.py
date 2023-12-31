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
from pydantic import BaseModel, Field, StrictStr, conlist, constr
from openapi_client.models.space_feature import SpaceFeature

class Seat(BaseModel):
    """
    Seat
    """
    type: Optional[StrictStr] = Field(None, alias="@type")
    location: Optional[constr(strict=True, max_length=32)] = Field(None, description="The seat location")
    seat_type: Optional[constr(strict=True, max_length=32)] = Field(None, alias="seatType", description="The type of seat")
    characteristic: Optional[conlist(constr(strict=True, max_length=1024), max_items=100)] = Field(None, alias="Characteristic")
    seat_feature: SpaceFeature = Field(..., alias="SeatFeature")
    __properties = ["@type", "location", "seatType", "Characteristic", "SeatFeature"]

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
    def from_json(cls, json_str: str) -> Seat:
        """Create an instance of Seat from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of seat_feature
        if self.seat_feature:
            _dict['SeatFeature'] = self.seat_feature.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Seat:
        """Create an instance of Seat from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Seat.parse_obj(obj)

        _obj = Seat.parse_obj({
            "type": obj.get("@type"),
            "location": obj.get("location"),
            "seat_type": obj.get("seatType"),
            "characteristic": obj.get("Characteristic"),
            "seat_feature": SpaceFeature.from_dict(obj.get("SeatFeature")) if obj.get("SeatFeature") is not None else None
        })
        return _obj


