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
from openapi_client.models.travel_document import TravelDocument
from openapi_client.models.traveler_updatable_item import TravelerUpdatableItem

class TravelerUpdatableItemTravelDocument(TravelerUpdatableItem):
    """
    TravelerUpdatableItemTravelDocument
    """
    travel_document: Optional[TravelDocument] = Field(None, alias="TravelDocument")
    __properties = ["@type", "Identifier", "addableInd", "modifiableInd", "deletableInd", "TravelDocument"]

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
    def from_json(cls, json_str: str) -> TravelerUpdatableItemTravelDocument:
        """Create an instance of TravelerUpdatableItemTravelDocument from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of travel_document
        if self.travel_document:
            _dict['TravelDocument'] = self.travel_document.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TravelerUpdatableItemTravelDocument:
        """Create an instance of TravelerUpdatableItemTravelDocument from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TravelerUpdatableItemTravelDocument.parse_obj(obj)

        _obj = TravelerUpdatableItemTravelDocument.parse_obj({
            "type": obj.get("@type"),
            "identifier": obj.get("Identifier"),
            "addable_ind": obj.get("addableInd"),
            "modifiable_ind": obj.get("modifiableInd"),
            "deletable_ind": obj.get("deletableInd"),
            "travel_document": TravelDocument.from_dict(obj.get("TravelDocument")) if obj.get("TravelDocument") is not None else None
        })
        return _obj

