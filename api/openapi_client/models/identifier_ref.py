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
from pydantic import BaseModel, Field, StrictStr, conlist, constr

class IdentifierRef(BaseModel):
    """
    IdentifierRef
    """
    value: Optional[constr(strict=True, max_length=128)] = None
    id: Optional[StrictStr] = Field(None, description="A locally referenced ID")
    description: Optional[StrictStr] = Field(None, description="Descriptive text used to identify the contents of a target object")
    uris: Optional[conlist(StrictStr)] = Field(None, description="Uniform Resource Identifier")
    __properties = ["value", "id", "description", "uris"]

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
    def from_json(cls, json_str: str) -> IdentifierRef:
        """Create an instance of IdentifierRef from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IdentifierRef:
        """Create an instance of IdentifierRef from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IdentifierRef.parse_obj(obj)

        _obj = IdentifierRef.parse_obj({
            "value": obj.get("value"),
            "id": obj.get("id"),
            "description": obj.get("description"),
            "uris": obj.get("uris")
        })
        return _obj

