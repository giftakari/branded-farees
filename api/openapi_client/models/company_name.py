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
from pydantic import BaseModel, Field, StrictStr, conlist, constr, validator

class CompanyName(BaseModel):
    """
    Identifies a company by name.
    """
    value: Optional[constr(strict=True, max_length=128)] = None
    id: Optional[StrictStr] = Field(None, description="Use this id to internally identify this company in NextSteps")
    division: Optional[constr(strict=True, max_length=32)] = Field(None, description="The division name or ID with which the contact is associated")
    department: Optional[constr(strict=True, max_length=32)] = Field(None, description="The department name or ID with which the contact is associated")
    short_name: Optional[constr(strict=True, max_length=32)] = Field(None, alias="shortName", description="Used to provide the company common name")
    code: Optional[constr(strict=True, max_length=32)] = Field(None, description="Identifies a company by the company code")
    code_context: Optional[constr(strict=True, max_length=32)] = Field(None, alias="codeContext", description="Identifies the context of the identifying code,such as DUNS,IATA or internal code")
    system_of_record: Optional[conlist(constr(strict=True, max_length=5, min_length=2))] = Field(None, alias="systemOfRecord", description="The system(s) that maintain the data")
    __properties = ["value", "id", "division", "department", "shortName", "code", "codeContext", "systemOfRecord"]

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
    def from_json(cls, json_str: str) -> CompanyName:
        """Create an instance of CompanyName from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CompanyName:
        """Create an instance of CompanyName from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CompanyName.parse_obj(obj)

        _obj = CompanyName.parse_obj({
            "value": obj.get("value"),
            "id": obj.get("id"),
            "division": obj.get("division"),
            "department": obj.get("department"),
            "short_name": obj.get("shortName"),
            "code": obj.get("code"),
            "code_context": obj.get("codeContext"),
            "system_of_record": obj.get("systemOfRecord")
        })
        return _obj

