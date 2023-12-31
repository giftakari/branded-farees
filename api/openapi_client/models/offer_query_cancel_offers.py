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
from pydantic import BaseModel, Field, StrictStr, conlist
from openapi_client.models.cancel_offer_request import CancelOfferRequest

class OfferQueryCancelOffers(BaseModel):
    """
    OfferQueryCancelOffers
    """
    type: StrictStr = Field(..., alias="@type")
    cancel_offer_request: conlist(CancelOfferRequest, max_items=100, min_items=1) = Field(..., alias="CancelOfferRequest")
    __properties = ["@type", "CancelOfferRequest"]

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
    def from_json(cls, json_str: str) -> OfferQueryCancelOffers:
        """Create an instance of OfferQueryCancelOffers from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in cancel_offer_request (list)
        _items = []
        if self.cancel_offer_request:
            for _item in self.cancel_offer_request:
                if _item:
                    _items.append(_item.to_dict())
            _dict['CancelOfferRequest'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OfferQueryCancelOffers:
        """Create an instance of OfferQueryCancelOffers from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OfferQueryCancelOffers.parse_obj(obj)

        _obj = OfferQueryCancelOffers.parse_obj({
            "type": obj.get("@type") if obj.get("@type") is not None else 'OfferQueryCancelOffers',
            "cancel_offer_request": [CancelOfferRequest.from_dict(_item) for _item in obj.get("CancelOfferRequest")] if obj.get("CancelOfferRequest") is not None else None
        })
        return _obj


