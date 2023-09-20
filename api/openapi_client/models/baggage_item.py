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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist, constr
from openapi_client.models.currency_amount import CurrencyAmount
from openapi_client.models.measurement import Measurement

class BaggageItem(BaseModel):
    """
    BaggageItem
    """
    type: Optional[StrictStr] = Field(None, alias="@type")
    quantity: Optional[StrictInt] = Field(None, description="Baggage item quantity")
    measurement: Optional[conlist(Measurement, max_items=6)] = Field(None, alias="Measurement")
    baggage_fee: Optional[CurrencyAmount] = Field(None, alias="BaggageFee")
    text: Optional[constr(strict=True, max_length=128)] = Field(None, alias="Text", description="Text returned from the shop response")
    __properties = ["@type", "quantity", "Measurement", "BaggageFee", "Text"]

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
    def from_json(cls, json_str: str) -> BaggageItem:
        """Create an instance of BaggageItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in measurement (list)
        _items = []
        if self.measurement:
            for _item in self.measurement:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Measurement'] = _items
        # override the default output from pydantic by calling `to_dict()` of baggage_fee
        if self.baggage_fee:
            _dict['BaggageFee'] = self.baggage_fee.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BaggageItem:
        """Create an instance of BaggageItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BaggageItem.parse_obj(obj)

        _obj = BaggageItem.parse_obj({
            "type": obj.get("@type"),
            "quantity": obj.get("quantity"),
            "measurement": [Measurement.from_dict(_item) for _item in obj.get("Measurement")] if obj.get("Measurement") is not None else None,
            "baggage_fee": CurrencyAmount.from_dict(obj.get("BaggageFee")) if obj.get("BaggageFee") is not None else None,
            "text": obj.get("Text")
        })
        return _obj


