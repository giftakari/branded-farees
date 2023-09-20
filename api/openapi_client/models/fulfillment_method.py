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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from openapi_client.models.change_fee_collection_method import ChangeFeeCollectionMethod
from openapi_client.models.refund_method_enum import RefundMethodEnum

class FulfillmentMethod(BaseModel):
    """
    FulfillmentMethod
    """
    type: Optional[StrictStr] = Field(None, alias="@type")
    product_refs: Optional[conlist(StrictStr)] = Field(None, alias="productRefs", description="The product(s) the Fulfillment Method applies to. If blank applies to all products in the Offer")
    segment_sequence_list: Optional[conlist(StrictInt)] = Field(None, alias="segmentSequenceList", description="List of segment sequence")
    refund_method: Optional[RefundMethodEnum] = Field(None, alias="RefundMethod")
    change_fee_collection_method: Optional[ChangeFeeCollectionMethod] = Field(None, alias="ChangeFeeCollectionMethod")
    __properties = ["@type", "productRefs", "segmentSequenceList", "RefundMethod", "ChangeFeeCollectionMethod"]

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
    def from_json(cls, json_str: str) -> FulfillmentMethod:
        """Create an instance of FulfillmentMethod from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of refund_method
        if self.refund_method:
            _dict['RefundMethod'] = self.refund_method.to_dict()
        # override the default output from pydantic by calling `to_dict()` of change_fee_collection_method
        if self.change_fee_collection_method:
            _dict['ChangeFeeCollectionMethod'] = self.change_fee_collection_method.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FulfillmentMethod:
        """Create an instance of FulfillmentMethod from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FulfillmentMethod.parse_obj(obj)

        _obj = FulfillmentMethod.parse_obj({
            "type": obj.get("@type"),
            "product_refs": obj.get("productRefs"),
            "segment_sequence_list": obj.get("segmentSequenceList"),
            "refund_method": RefundMethodEnum.from_dict(obj.get("RefundMethod")) if obj.get("RefundMethod") is not None else None,
            "change_fee_collection_method": ChangeFeeCollectionMethod.from_dict(obj.get("ChangeFeeCollectionMethod")) if obj.get("ChangeFeeCollectionMethod") is not None else None
        })
        return _obj

