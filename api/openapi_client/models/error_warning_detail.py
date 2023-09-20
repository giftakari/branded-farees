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
from pydantic import Field, constr
from openapi_client.models.error_warning import ErrorWarning
from openapi_client.models.name_value_pair import NameValuePair

class ErrorWarningDetail(ErrorWarning):
    """
    ErrorWarningDetail
    """
    source_id: constr(strict=True, max_length=128) = Field(..., alias="SourceID", description="The identifier of the source system sending the error or warning")
    source_code: Optional[constr(strict=True, max_length=32)] = Field(None, alias="SourceCode", description="The error or warning code returned by the source airline or host system")
    source_description: Optional[constr(strict=True, max_length=4096)] = Field(None, alias="SourceDescription", description="The error or warning message as it is returned by the source airline or host system")
    __properties = ["@type", "StatusCode", "Message", "NameValuePair", "SourceID", "SourceCode", "SourceDescription"]

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
    def from_json(cls, json_str: str) -> ErrorWarningDetail:
        """Create an instance of ErrorWarningDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in name_value_pair (list)
        _items = []
        if self.name_value_pair:
            for _item in self.name_value_pair:
                if _item:
                    _items.append(_item.to_dict())
            _dict['NameValuePair'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ErrorWarningDetail:
        """Create an instance of ErrorWarningDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ErrorWarningDetail.parse_obj(obj)

        _obj = ErrorWarningDetail.parse_obj({
            "type": obj.get("@type"),
            "status_code": obj.get("StatusCode"),
            "message": obj.get("Message"),
            "name_value_pair": [NameValuePair.from_dict(_item) for _item in obj.get("NameValuePair")] if obj.get("NameValuePair") is not None else None,
            "source_id": obj.get("SourceID"),
            "source_code": obj.get("SourceCode"),
            "source_description": obj.get("SourceDescription")
        })
        return _obj

