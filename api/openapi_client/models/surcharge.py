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
from pydantic import BaseModel, Field, StrictFloat, StrictInt, conint, constr, validator
from openapi_client.models.application_enum import ApplicationEnum
from openapi_client.models.frequency_enum import FrequencyEnum

class Surcharge(BaseModel):
    """
    The fee amount with feecode and reporting informtion
    """
    value: Optional[Union[StrictFloat, StrictInt]] = None
    currency_code: Optional[constr(strict=True)] = Field(None, alias="currencyCode", description="Sur charge currency code")
    surcharge_code: Optional[constr(strict=True, max_length=512)] = Field(None, alias="surchargeCode", description="Sur charge code")
    reporting_authority: Optional[constr(strict=True, max_length=512)] = Field(None, alias="reportingAuthority", description="Sur charge reporting authority")
    purpose: Optional[constr(strict=True, max_length=512)] = Field(None, description="Sur charge purpose")
    description: Optional[constr(strict=True, max_length=4096)] = Field(None, description="Description")
    surcharge_application: Optional[ApplicationEnum] = Field(None, alias="surchargeApplication")
    surcharge_frequency: Optional[FrequencyEnum] = Field(None, alias="surchargeFrequency")
    code_authority: Optional[constr(strict=True, max_length=32)] = Field(None, alias="codeAuthority", description="Surcharge code authority")
    decimal_place: Optional[conint(strict=True, ge=0)] = Field(None, alias="decimalPlace", description="Decimal place for the currency unit")
    decimal_authority: Optional[constr(strict=True, max_length=32)] = Field(None, alias="decimalAuthority", description="Currency code decimal authority")
    __properties = ["value", "currencyCode", "surchargeCode", "reportingAuthority", "purpose", "description", "surchargeApplication", "surchargeFrequency", "codeAuthority", "decimalPlace", "decimalAuthority"]

    @validator('currency_code')
    def currency_code_validate_regular_expression(cls, value):
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
    def from_json(cls, json_str: str) -> Surcharge:
        """Create an instance of Surcharge from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Surcharge:
        """Create an instance of Surcharge from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Surcharge.parse_obj(obj)

        _obj = Surcharge.parse_obj({
            "value": obj.get("value"),
            "currency_code": obj.get("currencyCode"),
            "surcharge_code": obj.get("surchargeCode"),
            "reporting_authority": obj.get("reportingAuthority"),
            "purpose": obj.get("purpose"),
            "description": obj.get("description"),
            "surcharge_application": obj.get("surchargeApplication"),
            "surcharge_frequency": obj.get("surchargeFrequency"),
            "code_authority": obj.get("codeAuthority"),
            "decimal_place": obj.get("decimalPlace"),
            "decimal_authority": obj.get("decimalAuthority")
        })
        return _obj


