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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class DisplaySequence(BaseModel):
    """
    DisplaySequence
    """
    type: Optional[StrictStr] = Field(None, alias="@type")
    display_sequence: StrictStr = Field(..., alias="displaySequence", description="The sequence the products are to be displayed for sequential date ordering")
    offer_ref: StrictStr = Field(..., alias="OfferRef", description="Offer reference")
    product_ref: Optional[StrictStr] = Field(None, alias="ProductRef", description="Product reference. If blank, display sequence applies to all products within the Offer.")
    sequence: Optional[StrictInt] = Field(None, alias="Sequence", description="Segment sequence, if blank, display sequence applies to all segments within the product")
    __properties = ["@type", "displaySequence", "OfferRef", "ProductRef", "Sequence"]

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
    def from_json(cls, json_str: str) -> DisplaySequence:
        """Create an instance of DisplaySequence from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DisplaySequence:
        """Create an instance of DisplaySequence from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DisplaySequence.parse_obj(obj)

        _obj = DisplaySequence.parse_obj({
            "type": obj.get("@type"),
            "display_sequence": obj.get("displaySequence"),
            "offer_ref": obj.get("OfferRef"),
            "product_ref": obj.get("ProductRef"),
            "sequence": obj.get("Sequence")
        })
        return _obj


