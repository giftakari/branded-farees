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


from typing import List
from pydantic import BaseModel, Field, conlist
from openapi_client.models.organization_loyalty_program import OrganizationLoyaltyProgram

class OrganizationLoyaltyProgramListRequest(BaseModel):
    """
    OrganizationLoyaltyProgramListRequest
    """
    organization_loyalty_program: conlist(OrganizationLoyaltyProgram, max_items=10, min_items=1) = Field(..., alias="OrganizationLoyaltyProgram")
    __properties = ["OrganizationLoyaltyProgram"]

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
    def from_json(cls, json_str: str) -> OrganizationLoyaltyProgramListRequest:
        """Create an instance of OrganizationLoyaltyProgramListRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in organization_loyalty_program (list)
        _items = []
        if self.organization_loyalty_program:
            for _item in self.organization_loyalty_program:
                if _item:
                    _items.append(_item.to_dict())
            _dict['OrganizationLoyaltyProgram'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrganizationLoyaltyProgramListRequest:
        """Create an instance of OrganizationLoyaltyProgramListRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrganizationLoyaltyProgramListRequest.parse_obj(obj)

        _obj = OrganizationLoyaltyProgramListRequest.parse_obj({
            "organization_loyalty_program": [OrganizationLoyaltyProgram.from_dict(_item) for _item in obj.get("OrganizationLoyaltyProgram")] if obj.get("OrganizationLoyaltyProgram") is not None else None
        })
        return _obj

