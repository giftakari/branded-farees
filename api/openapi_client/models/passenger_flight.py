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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist, constr, validator
from openapi_client.models.flight_product import FlightProduct

class PassengerFlight(BaseModel):
    """
    PassengerFlight
    """
    type: Optional[StrictStr] = Field(None, alias="@type")
    passenger_quantity: Optional[StrictInt] = Field(None, alias="passengerQuantity", description="Number of passengers of the specified passenger type code")
    passenger_type_code: Optional[constr(strict=True, max_length=5, min_length=3)] = Field(None, alias="passengerTypeCode", description="Passenger type code")
    flight_product: Optional[conlist(FlightProduct, max_items=99)] = Field(None, alias="FlightProduct")
    __properties = ["@type", "passengerQuantity", "passengerTypeCode", "FlightProduct"]

    @validator('passenger_type_code')
    def passenger_type_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"([a-zA-Z0-9]{3,5})", value):
            raise ValueError(r"must validate the regular expression /([a-zA-Z0-9]{3,5})/")
        return value

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
    def from_json(cls, json_str: str) -> PassengerFlight:
        """Create an instance of PassengerFlight from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in flight_product (list)
        _items = []
        if self.flight_product:
            for _item in self.flight_product:
                if _item:
                    _items.append(_item.to_dict())
            _dict['FlightProduct'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PassengerFlight:
        """Create an instance of PassengerFlight from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PassengerFlight.parse_obj(obj)

        _obj = PassengerFlight.parse_obj({
            "type": obj.get("@type"),
            "passenger_quantity": obj.get("passengerQuantity"),
            "passenger_type_code": obj.get("passengerTypeCode"),
            "flight_product": [FlightProduct.from_dict(_item) for _item in obj.get("FlightProduct")] if obj.get("FlightProduct") is not None else None
        })
        return _obj


