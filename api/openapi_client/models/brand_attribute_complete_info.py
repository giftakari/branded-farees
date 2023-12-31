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
from pydantic import Field, conlist, constr
from openapi_client.models.brand_attribute import BrandAttribute
from openapi_client.models.brand_classification_enum import BrandClassificationEnum
from openapi_client.models.brand_inclusion_enum import BrandInclusionEnum
from openapi_client.models.brand_text import BrandText

class BrandAttributeCompleteInfo(BrandAttribute):
    """
    BrandAttributeCompleteInfo
    """
    name: Optional[constr(strict=True, max_length=128)] = Field(None, description="Assigned Type: ctbr-1100:BrandAttributeName")
    attribute_text: conlist(BrandText, max_items=100, min_items=1) = Field(..., alias="AttributeText")
    __properties = ["@type", "classification", "inclusion", "ImageURL", "matchedAttributeInd", "groupCode", "subGroupCode", "subCode", "name", "AttributeText"]

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
    def from_json(cls, json_str: str) -> BrandAttributeCompleteInfo:
        """Create an instance of BrandAttributeCompleteInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in attribute_text (list)
        _items = []
        if self.attribute_text:
            for _item in self.attribute_text:
                if _item:
                    _items.append(_item.to_dict())
            _dict['AttributeText'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BrandAttributeCompleteInfo:
        """Create an instance of BrandAttributeCompleteInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BrandAttributeCompleteInfo.parse_obj(obj)

        _obj = BrandAttributeCompleteInfo.parse_obj({
            "type": obj.get("@type"),
            "classification": obj.get("classification"),
            "inclusion": obj.get("inclusion"),
            "image_url": obj.get("ImageURL"),
            "matched_attribute_ind": obj.get("matchedAttributeInd"),
            "group_code": obj.get("groupCode"),
            "sub_group_code": obj.get("subGroupCode"),
            "sub_code": obj.get("subCode"),
            "name": obj.get("name"),
            "attribute_text": [BrandText.from_dict(_item) for _item in obj.get("AttributeText")] if obj.get("AttributeText") is not None else None
        })
        return _obj


