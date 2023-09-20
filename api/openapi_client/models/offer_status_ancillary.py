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


from typing import List
from pydantic import Field, conlist
from openapi_client.models.offer_status import OfferStatus
from openapi_client.models.status_ancillary import StatusAncillary

class OfferStatusAncillary(OfferStatus):
    """
    OfferStatusAncillary
    """
    status_ancillary: conlist(StatusAncillary, max_items=10, min_items=1) = Field(..., alias="StatusAncillary")
    __properties = ["@type", "StatusAncillary"]

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
    def from_json(cls, json_str: str) -> OfferStatusAncillary:
        """Create an instance of OfferStatusAncillary from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in status_ancillary (list)
        _items = []
        if self.status_ancillary:
            for _item in self.status_ancillary:
                if _item:
                    _items.append(_item.to_dict())
            _dict['StatusAncillary'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OfferStatusAncillary:
        """Create an instance of OfferStatusAncillary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OfferStatusAncillary.parse_obj(obj)

        _obj = OfferStatusAncillary.parse_obj({
            "type": obj.get("@type"),
            "status_ancillary": [StatusAncillary.from_dict(_item) for _item in obj.get("StatusAncillary")] if obj.get("StatusAncillary") is not None else None
        })
        return _obj


