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
from pydantic import BaseModel, Field, StrictStr, conlist
from openapi_client.models.gst_registration_number import GSTRegistrationNumber
from openapi_client.models.organization_identifier import OrganizationIdentifier

class OrganizationInformation(BaseModel):
    """
    OrganizationInformation
    """
    type: Optional[StrictStr] = Field(None, alias="@type")
    organization_identifier: Optional[conlist(OrganizationIdentifier, max_items=10)] = Field(None, alias="OrganizationIdentifier")
    gst_registration_number: Optional[conlist(GSTRegistrationNumber, max_items=10)] = Field(None, alias="GSTRegistrationNumber")
    __properties = ["@type", "OrganizationIdentifier", "GSTRegistrationNumber"]

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
    def from_json(cls, json_str: str) -> OrganizationInformation:
        """Create an instance of OrganizationInformation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in organization_identifier (list)
        _items = []
        if self.organization_identifier:
            for _item in self.organization_identifier:
                if _item:
                    _items.append(_item.to_dict())
            _dict['OrganizationIdentifier'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in gst_registration_number (list)
        _items = []
        if self.gst_registration_number:
            for _item in self.gst_registration_number:
                if _item:
                    _items.append(_item.to_dict())
            _dict['GSTRegistrationNumber'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrganizationInformation:
        """Create an instance of OrganizationInformation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrganizationInformation.parse_obj(obj)

        _obj = OrganizationInformation.parse_obj({
            "type": obj.get("@type"),
            "organization_identifier": [OrganizationIdentifier.from_dict(_item) for _item in obj.get("OrganizationIdentifier")] if obj.get("OrganizationIdentifier") is not None else None,
            "gst_registration_number": [GSTRegistrationNumber.from_dict(_item) for _item in obj.get("GSTRegistrationNumber")] if obj.get("GSTRegistrationNumber") is not None else None
        })
        return _obj

