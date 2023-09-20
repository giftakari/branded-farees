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



from pydantic import Field
from openapi_client.models.applies_to import AppliesTo
from openapi_client.models.preference import Preference
from openapi_client.models.seat_location_enum import SeatLocationEnum
from openapi_client.models.traveler_identifier import TravelerIdentifier

class PreferenceAirSeat(Preference):
    """
    PreferenceAirSeat
    """
    seat_location: SeatLocationEnum = Field(..., alias="SeatLocation")
    __properties = ["@type", "id", "AppliesTo", "TravelerIdentifier", "SeatLocation"]

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
    def from_json(cls, json_str: str) -> PreferenceAirSeat:
        """Create an instance of PreferenceAirSeat from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of applies_to
        if self.applies_to:
            _dict['AppliesTo'] = self.applies_to.to_dict()
        # override the default output from pydantic by calling `to_dict()` of traveler_identifier
        if self.traveler_identifier:
            _dict['TravelerIdentifier'] = self.traveler_identifier.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PreferenceAirSeat:
        """Create an instance of PreferenceAirSeat from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PreferenceAirSeat.parse_obj(obj)

        _obj = PreferenceAirSeat.parse_obj({
            "type": obj.get("@type"),
            "id": obj.get("id"),
            "applies_to": AppliesTo.from_dict(obj.get("AppliesTo")) if obj.get("AppliesTo") is not None else None,
            "traveler_identifier": TravelerIdentifier.from_dict(obj.get("TravelerIdentifier")) if obj.get("TravelerIdentifier") is not None else None,
            "seat_location": obj.get("SeatLocation")
        })
        return _obj


