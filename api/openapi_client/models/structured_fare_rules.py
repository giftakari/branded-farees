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
from pydantic import BaseModel, Field, StrictStr, conlist, constr, validator
from openapi_client.models.advance_payment import AdvancePayment
from openapi_client.models.advance_reservation import AdvanceReservation
from openapi_client.models.maximum_stay import MaximumStay
from openapi_client.models.minimum_stay import MinimumStay
from openapi_client.models.penalties import Penalties
from openapi_client.models.stopover import Stopover

class StructuredFareRules(BaseModel):
    """
    StructuredFareRules
    """
    type: Optional[StrictStr] = Field(None, alias="@type")
    passenger_type_codes: Optional[conlist(constr(strict=True, max_length=5, min_length=3))] = Field(None, alias="passengerTypeCodes", description="List of passenger type codes")
    penalties: Optional[conlist(Penalties, max_items=10)] = Field(None, alias="Penalties")
    minimum_stay: Optional[conlist(MinimumStay, max_items=10)] = Field(None, alias="MinimumStay")
    maximum_stay: Optional[conlist(MaximumStay, max_items=10)] = Field(None, alias="MaximumStay")
    advance_reservation: Optional[conlist(AdvanceReservation, max_items=10)] = Field(None, alias="AdvanceReservation")
    advance_payment: Optional[conlist(AdvancePayment, max_items=10)] = Field(None, alias="AdvancePayment")
    stopover: Optional[conlist(Stopover, max_items=10)] = Field(None, alias="Stopover")
    __properties = ["@type", "passengerTypeCodes", "Penalties", "MinimumStay", "MaximumStay", "AdvanceReservation", "AdvancePayment", "Stopover"]

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
    def from_json(cls, json_str: str) -> StructuredFareRules:
        """Create an instance of StructuredFareRules from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in penalties (list)
        _items = []
        if self.penalties:
            for _item in self.penalties:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Penalties'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in minimum_stay (list)
        _items = []
        if self.minimum_stay:
            for _item in self.minimum_stay:
                if _item:
                    _items.append(_item.to_dict())
            _dict['MinimumStay'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in maximum_stay (list)
        _items = []
        if self.maximum_stay:
            for _item in self.maximum_stay:
                if _item:
                    _items.append(_item.to_dict())
            _dict['MaximumStay'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in advance_reservation (list)
        _items = []
        if self.advance_reservation:
            for _item in self.advance_reservation:
                if _item:
                    _items.append(_item.to_dict())
            _dict['AdvanceReservation'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in advance_payment (list)
        _items = []
        if self.advance_payment:
            for _item in self.advance_payment:
                if _item:
                    _items.append(_item.to_dict())
            _dict['AdvancePayment'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in stopover (list)
        _items = []
        if self.stopover:
            for _item in self.stopover:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Stopover'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StructuredFareRules:
        """Create an instance of StructuredFareRules from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StructuredFareRules.parse_obj(obj)

        _obj = StructuredFareRules.parse_obj({
            "type": obj.get("@type"),
            "passenger_type_codes": obj.get("passengerTypeCodes"),
            "penalties": [Penalties.from_dict(_item) for _item in obj.get("Penalties")] if obj.get("Penalties") is not None else None,
            "minimum_stay": [MinimumStay.from_dict(_item) for _item in obj.get("MinimumStay")] if obj.get("MinimumStay") is not None else None,
            "maximum_stay": [MaximumStay.from_dict(_item) for _item in obj.get("MaximumStay")] if obj.get("MaximumStay") is not None else None,
            "advance_reservation": [AdvanceReservation.from_dict(_item) for _item in obj.get("AdvanceReservation")] if obj.get("AdvanceReservation") is not None else None,
            "advance_payment": [AdvancePayment.from_dict(_item) for _item in obj.get("AdvancePayment")] if obj.get("AdvancePayment") is not None else None,
            "stopover": [Stopover.from_dict(_item) for _item in obj.get("Stopover")] if obj.get("Stopover") is not None else None
        })
        return _obj

