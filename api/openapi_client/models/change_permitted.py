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
from pydantic import Field, StrictBool, conlist
from openapi_client.models.change import Change
from openapi_client.models.penalty import Penalty
from openapi_client.models.penalty_applies_to_enum import PenaltyAppliesToEnum
from openapi_client.models.penalty_type_enum import PenaltyTypeEnum

class ChangePermitted(Change):
    """
    ChangePermitted
    """
    penalty_types: conlist(PenaltyTypeEnum) = Field(..., alias="penaltyTypes")
    penalty_applies_to: Optional[PenaltyAppliesToEnum] = Field(None, alias="PenaltyAppliesTo")
    penalty: Optional[conlist(Penalty, max_items=2)] = Field(None, alias="Penalty")
    higher_penatlty_applies_ind: Optional[StrictBool] = Field(None, alias="higherPenatltyAppliesInd", description="If true, when an amount and a percent are specified in the Penalty then the higher of these apply")
    __properties = ["@type", "ProductRefs", "SegmentSequence", "penaltyTypes", "PenaltyAppliesTo", "Penalty", "higherPenatltyAppliesInd"]

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
    def from_json(cls, json_str: str) -> ChangePermitted:
        """Create an instance of ChangePermitted from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in penalty (list)
        _items = []
        if self.penalty:
            for _item in self.penalty:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Penalty'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ChangePermitted:
        """Create an instance of ChangePermitted from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ChangePermitted.parse_obj(obj)

        _obj = ChangePermitted.parse_obj({
            "type": obj.get("@type"),
            "product_refs": obj.get("ProductRefs"),
            "segment_sequence": obj.get("SegmentSequence"),
            "penalty_types": obj.get("penaltyTypes"),
            "penalty_applies_to": obj.get("PenaltyAppliesTo"),
            "penalty": [Penalty.from_dict(_item) for _item in obj.get("Penalty")] if obj.get("Penalty") is not None else None,
            "higher_penatlty_applies_ind": obj.get("higherPenatltyAppliesInd")
        })
        return _obj

