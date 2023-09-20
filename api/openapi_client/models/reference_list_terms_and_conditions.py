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
from pydantic import Field, conlist
from openapi_client.models.reference_list import ReferenceList
from openapi_client.models.terms_and_conditions import TermsAndConditions

class ReferenceListTermsAndConditions(ReferenceList):
    """
    ReferenceListTermsAndConditions
    """
    terms_and_conditions: Optional[conlist(TermsAndConditions)] = Field(None, alias="TermsAndConditions")
    __properties = ["@type", "id", "TermsAndConditions"]

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
    def from_json(cls, json_str: str) -> ReferenceListTermsAndConditions:
        """Create an instance of ReferenceListTermsAndConditions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in terms_and_conditions (list)
        _items = []
        if self.terms_and_conditions:
            for _item in self.terms_and_conditions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['TermsAndConditions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReferenceListTermsAndConditions:
        """Create an instance of ReferenceListTermsAndConditions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReferenceListTermsAndConditions.parse_obj(obj)

        _obj = ReferenceListTermsAndConditions.parse_obj({
            "type": obj.get("@type"),
            "id": obj.get("id"),
            "terms_and_conditions": [TermsAndConditions.from_dict(_item) for _item in obj.get("TermsAndConditions")] if obj.get("TermsAndConditions") is not None else None
        })
        return _obj

