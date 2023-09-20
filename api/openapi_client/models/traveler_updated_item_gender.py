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
from pydantic import Field
from openapi_client.models.gender_enum import GenderEnum
from openapi_client.models.traveler_updated_item import TravelerUpdatedItem

class TravelerUpdatedItemGender(TravelerUpdatedItem):
    """
    TravelerUpdatedItemGender
    """
    gender_updatable: Optional[GenderEnum] = Field(None, alias="GenderUpdatable")
    __properties = ["@type", "TravelerUpdatableItemID", "addInd", "modifyInd", "deleteInd", "GenderUpdatable"]

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
    def from_json(cls, json_str: str) -> TravelerUpdatedItemGender:
        """Create an instance of TravelerUpdatedItemGender from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TravelerUpdatedItemGender:
        """Create an instance of TravelerUpdatedItemGender from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TravelerUpdatedItemGender.parse_obj(obj)

        _obj = TravelerUpdatedItemGender.parse_obj({
            "type": obj.get("@type"),
            "traveler_updatable_item_id": obj.get("TravelerUpdatableItemID"),
            "add_ind": obj.get("addInd"),
            "modify_ind": obj.get("modifyInd"),
            "delete_ind": obj.get("deleteInd"),
            "gender_updatable": obj.get("GenderUpdatable")
        })
        return _obj


