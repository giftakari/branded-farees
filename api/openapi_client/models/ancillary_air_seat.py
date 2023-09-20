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
from openapi_client.models.ancillary_air import AncillaryAir
from openapi_client.models.ancillary_description import AncillaryDescription
from openapi_client.models.seat_assignment import SeatAssignment

class AncillaryAirSeat(AncillaryAir):
    """
    AncillaryAirSeat
    """
    seat_assignment: SeatAssignment = Field(..., alias="SeatAssignment")
    __properties = ["@type", "quantity", "Description", "FlightRef", "SeatAssignment"]

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
    def from_json(cls, json_str: str) -> AncillaryAirSeat:
        """Create an instance of AncillaryAirSeat from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in description (list)
        _items = []
        if self.description:
            for _item in self.description:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Description'] = _items
        # override the default output from pydantic by calling `to_dict()` of seat_assignment
        if self.seat_assignment:
            _dict['SeatAssignment'] = self.seat_assignment.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AncillaryAirSeat:
        """Create an instance of AncillaryAirSeat from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AncillaryAirSeat.parse_obj(obj)

        _obj = AncillaryAirSeat.parse_obj({
            "type": obj.get("@type"),
            "quantity": obj.get("quantity"),
            "description": [AncillaryDescription.from_dict(_item) for _item in obj.get("Description")] if obj.get("Description") is not None else None,
            "flight_ref": obj.get("FlightRef"),
            "seat_assignment": SeatAssignment.from_dict(obj.get("SeatAssignment")) if obj.get("SeatAssignment") is not None else None
        })
        return _obj

