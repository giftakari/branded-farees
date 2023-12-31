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
from openapi_client.models.traveler_updatable_items_list_response import TravelerUpdatableItemsListResponse

class TravelerUpdatableItemsListResponseWrapper(BaseModel):
    """
    TravelerUpdatableItemsListResponseWrapper
    """
    traveler_updatable_items_list_response: Optional[TravelerUpdatableItemsListResponse] = Field(None, alias="TravelerUpdatableItemsListResponse")
    __properties = ["TravelerUpdatableItemsListResponse"]

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
    def from_json(cls, json_str: str) -> TravelerUpdatableItemsListResponseWrapper:
        """Create an instance of TravelerUpdatableItemsListResponseWrapper from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of traveler_updatable_items_list_response
        if self.traveler_updatable_items_list_response:
            _dict['TravelerUpdatableItemsListResponse'] = self.traveler_updatable_items_list_response.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TravelerUpdatableItemsListResponseWrapper:
        """Create an instance of TravelerUpdatableItemsListResponseWrapper from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TravelerUpdatableItemsListResponseWrapper.parse_obj(obj)

        _obj = TravelerUpdatableItemsListResponseWrapper.parse_obj({
            "traveler_updatable_items_list_response": TravelerUpdatableItemsListResponse.from_dict(obj.get("TravelerUpdatableItemsListResponse")) if obj.get("TravelerUpdatableItemsListResponse") is not None else None
        })
        return _obj


