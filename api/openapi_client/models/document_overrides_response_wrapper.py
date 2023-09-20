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
from pydantic import BaseModel, Field
from openapi_client.models.document_overrides_response import DocumentOverridesResponse

class DocumentOverridesResponseWrapper(BaseModel):
    """
    DocumentOverridesResponseWrapper
    """
    document_overrides_response: Optional[DocumentOverridesResponse] = Field(None, alias="DocumentOverridesResponse")
    __properties = ["DocumentOverridesResponse"]

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
    def from_json(cls, json_str: str) -> DocumentOverridesResponseWrapper:
        """Create an instance of DocumentOverridesResponseWrapper from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of document_overrides_response
        if self.document_overrides_response:
            _dict['DocumentOverridesResponse'] = self.document_overrides_response.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DocumentOverridesResponseWrapper:
        """Create an instance of DocumentOverridesResponseWrapper from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DocumentOverridesResponseWrapper.parse_obj(obj)

        _obj = DocumentOverridesResponseWrapper.parse_obj({
            "document_overrides_response": DocumentOverridesResponse.from_dict(obj.get("DocumentOverridesResponse")) if obj.get("DocumentOverridesResponse") is not None else None
        })
        return _obj


