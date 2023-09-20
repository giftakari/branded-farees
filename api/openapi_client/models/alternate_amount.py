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

class AlternateAmount(BaseModel):
    """
    AlternateAmount
    """
    amount: Union[StrictFloat, StrictInt] = Field(..., description="The base amount")
    currency_code: constr(strict=True) = Field(..., alias="currencyCode", description="Amount currency code")
    decimal_place: conint(strict=True, ge=0) = Field(..., alias="decimalPlace", description="ISO 4217 decimal standard")
    fare_calculation: Optional[constr(strict=True, max_length=128)] = Field(None, alias="fareCalculation", description="the fare calculation string")
    rate_of_exchange: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="rateOfExchange", description="The rate of exchange used to convert the fare calculation")
    __properties = ["amount", "currencyCode", "decimalPlace", "fareCalculation", "rateOfExchange"]

    @validator('currency_code')
    def currency_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
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
    def from_json(cls, json_str: str) -> AlternateAmount:
        """Create an instance of AlternateAmount from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AlternateAmount:
        """Create an instance of AlternateAmount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AlternateAmount.parse_obj(obj)

        _obj = AlternateAmount.parse_obj({
            "amount": obj.get("amount"),
            "currency_code": obj.get("currencyCode"),
            "decimal_place": obj.get("decimalPlace"),
            "fare_calculation": obj.get("fareCalculation"),
            "rate_of_exchange": obj.get("rateOfExchange")
        })
        return _obj


