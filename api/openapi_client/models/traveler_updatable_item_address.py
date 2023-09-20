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
from openapi_client.models.address import Address
from openapi_client.models.traveler_updatable_item import TravelerUpdatableItem

class TravelerUpdatableItemAddress(TravelerUpdatableItem):
    """
    TravelerUpdatableItemAddress
    """
    address: Optional[Address] = Field(None, alias="Address")
    __properties = ["@type", "Identifier", "addableInd", "modifiableInd", "deletableInd", "Address"]

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
    def from_json(cls, json_str: str) -> TravelerUpdatableItemAddress:
        """Create an instance of TravelerUpdatableItemAddress from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['Address'] = self.address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TravelerUpdatableItemAddress:
        """Create an instance of TravelerUpdatableItemAddress from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TravelerUpdatableItemAddress.parse_obj(obj)

        _obj = TravelerUpdatableItemAddress.parse_obj({
            "type": obj.get("@type"),
            "identifier": obj.get("Identifier"),
            "addable_ind": obj.get("addableInd"),
            "modifiable_ind": obj.get("modifiableInd"),
            "deletable_ind": obj.get("deletableInd"),
            "address": Address.from_dict(obj.get("Address")) if obj.get("Address") is not None else None
        })
        return _obj


