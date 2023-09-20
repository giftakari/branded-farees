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
from pydantic import BaseModel, Field, conint, constr, validator

class CurrencyCode(BaseModel):
    """
    Currency codes are the three-letter alphabetic codes that represent the various currencies used throughout the world.
    """
    value: Optional[constr(strict=True)] = None
    code_authority: Optional[constr(strict=True, max_length=32)] = Field(None, alias="codeAuthority", description="Currency code authority")
    decimal_place: Optional[conint(strict=True, ge=0)] = Field(None, alias="decimalPlace", description="Currency code decimal place")
    decimal_authority: Optional[constr(strict=True, max_length=32)] = Field(None, alias="decimalAuthority", description="Currency code decimal authority")
    __properties = ["value", "codeAuthority", "decimalPlace", "decimalAuthority"]

    @validator('value')
    def value_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[a-zA-Z]{3}", value):
            raise ValueError(r"must validate the regular expression /[a-zA-Z]{3}/")
        return value

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
    def from_json(cls, json_str: str) -> CurrencyCode:
        """Create an instance of CurrencyCode from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CurrencyCode:
        """Create an instance of CurrencyCode from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CurrencyCode.parse_obj(obj)

        _obj = CurrencyCode.parse_obj({
            "value": obj.get("value"),
            "code_authority": obj.get("codeAuthority"),
            "decimal_place": obj.get("decimalPlace"),
            "decimal_authority": obj.get("decimalAuthority")
        })
        return _obj

