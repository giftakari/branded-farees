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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, constr
from openapi_client.models.offer_status_enum import OfferStatusEnum

class StatusAir(BaseModel):
    """
    StatusAir
    """
    value: Optional[OfferStatusEnum] = None
    flight_refs: Optional[conlist(StrictStr)] = Field(None, alias="flightRefs", description="The flightRefs the status is applicable to within the Offer")
    code: Optional[constr(strict=True, max_length=32)] = Field(None, description="Status code")
    past_date_ind: Optional[StrictBool] = Field(None, alias="pastDateInd", description="If true, the flight is considered to be past date")
    __properties = ["value", "flightRefs", "code", "pastDateInd"]

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
    def from_json(cls, json_str: str) -> StatusAir:
        """Create an instance of StatusAir from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StatusAir:
        """Create an instance of StatusAir from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StatusAir.parse_obj(obj)

        _obj = StatusAir.parse_obj({
            "value": obj.get("value"),
            "flight_refs": obj.get("flightRefs"),
            "code": obj.get("code"),
            "past_date_ind": obj.get("pastDateInd")
        })
        return _obj


