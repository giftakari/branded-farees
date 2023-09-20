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
from pydantic import Field, StrictStr
from openapi_client.models.baggage_allowance import BaggageAllowance
from openapi_client.models.baggage_item import BaggageItem
from openapi_client.models.baggage_type_enum import BaggageTypeEnum

class BaggageAllowanceDetail(BaggageAllowance):
    """
    BaggageAllowanceDetail
    """
    url: Optional[StrictStr] = Field(None, description="Url for the airline's baggage information web site")
    __properties = ["@type", "passengerTypeCodes", "baggageType", "ProductRef", "BaggageItem", "SegmentSequenceList", "Text", "url"]

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
    def from_json(cls, json_str: str) -> BaggageAllowanceDetail:
        """Create an instance of BaggageAllowanceDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in baggage_item (list)
        _items = []
        if self.baggage_item:
            for _item in self.baggage_item:
                if _item:
                    _items.append(_item.to_dict())
            _dict['BaggageItem'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BaggageAllowanceDetail:
        """Create an instance of BaggageAllowanceDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BaggageAllowanceDetail.parse_obj(obj)

        _obj = BaggageAllowanceDetail.parse_obj({
            "type": obj.get("@type"),
            "passenger_type_codes": obj.get("passengerTypeCodes"),
            "baggage_type": obj.get("baggageType"),
            "product_ref": obj.get("ProductRef"),
            "baggage_item": [BaggageItem.from_dict(_item) for _item in obj.get("BaggageItem")] if obj.get("BaggageItem") is not None else None,
            "segment_sequence_list": obj.get("SegmentSequenceList"),
            "text": obj.get("Text"),
            "url": obj.get("url")
        })
        return _obj

