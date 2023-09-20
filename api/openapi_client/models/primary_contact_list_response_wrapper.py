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
from pydantic import BaseModel, Field
from openapi_client.models.primary_contact_list_response import PrimaryContactListResponse

class PrimaryContactListResponseWrapper(BaseModel):
    """
    PrimaryContactListResponseWrapper
    """
    primary_contact_list_response: Optional[PrimaryContactListResponse] = Field(None, alias="PrimaryContactListResponse")
    __properties = ["PrimaryContactListResponse"]

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
    def from_json(cls, json_str: str) -> PrimaryContactListResponseWrapper:
        """Create an instance of PrimaryContactListResponseWrapper from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of primary_contact_list_response
        if self.primary_contact_list_response:
            _dict['PrimaryContactListResponse'] = self.primary_contact_list_response.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PrimaryContactListResponseWrapper:
        """Create an instance of PrimaryContactListResponseWrapper from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PrimaryContactListResponseWrapper.parse_obj(obj)

        _obj = PrimaryContactListResponseWrapper.parse_obj({
            "primary_contact_list_response": PrimaryContactListResponse.from_dict(obj.get("PrimaryContactListResponse")) if obj.get("PrimaryContactListResponse") is not None else None
        })
        return _obj

