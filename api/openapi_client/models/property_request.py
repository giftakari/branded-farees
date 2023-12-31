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
from openapi_client.models.property_key import PropertyKey

class PropertyRequest(BaseModel):
    """
    PropertyRequest
    """
    type: Optional[StrictStr] = Field(None, alias="@type")
    more_rates_token: Optional[constr(strict=True, max_length=512)] = Field(None, alias="moreRatesToken", description="More rates token")
    property_key: PropertyKey = Field(..., alias="PropertyKey")
    __properties = ["@type", "moreRatesToken", "PropertyKey"]

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
    def from_json(cls, json_str: str) -> PropertyRequest:
        """Create an instance of PropertyRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of property_key
        if self.property_key:
            _dict['PropertyKey'] = self.property_key.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PropertyRequest:
        """Create an instance of PropertyRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PropertyRequest.parse_obj(obj)

        _obj = PropertyRequest.parse_obj({
            "type": obj.get("@type"),
            "more_rates_token": obj.get("moreRatesToken"),
            "property_key": PropertyKey.from_dict(obj.get("PropertyKey")) if obj.get("PropertyKey") is not None else None
        })
        return _obj


