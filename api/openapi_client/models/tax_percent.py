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


from typing import Optional, Union
from pydantic import BaseModel, Field, confloat, conint, constr
from openapi_client.models.yes_no_unknown_enum import YesNoUnknownEnum

class TaxPercent(BaseModel):
    """
    TaxPercent
    """
    value: Optional[Union[confloat(ge=0, strict=True), conint(ge=0, strict=True)]] = None
    tax_code: Optional[constr(strict=True, max_length=512)] = Field(None, alias="taxCode", description="Tax code")
    reporting_authority: Optional[constr(strict=True, max_length=512)] = Field(None, alias="reportingAuthority", description="Tax reporting authority")
    purpose: Optional[constr(strict=True, max_length=512)] = Field(None, description="Purpose of tax")
    description: Optional[constr(strict=True, max_length=4096)] = Field(None, description="Description")
    included_in_base: Optional[YesNoUnknownEnum] = Field(None, alias="includedInBase")
    __properties = ["value", "taxCode", "reportingAuthority", "purpose", "description", "includedInBase"]

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
    def from_json(cls, json_str: str) -> TaxPercent:
        """Create an instance of TaxPercent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TaxPercent:
        """Create an instance of TaxPercent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TaxPercent.parse_obj(obj)

        _obj = TaxPercent.parse_obj({
            "value": obj.get("value"),
            "tax_code": obj.get("taxCode"),
            "reporting_authority": obj.get("reportingAuthority"),
            "purpose": obj.get("purpose"),
            "description": obj.get("description"),
            "included_in_base": obj.get("includedInBase")
        })
        return _obj

