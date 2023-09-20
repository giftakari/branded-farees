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
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from openapi_client.models.currency_code import CurrencyCode
from openapi_client.models.currency_source_enum import CurrencySourceEnum
from openapi_client.models.fees import Fees
from openapi_client.models.taxes import Taxes

class Amount(BaseModel):
    """
    Amount
    """
    type: Optional[StrictStr] = Field(None, alias="@type")
    currency_source: Optional[CurrencySourceEnum] = Field(None, alias="currencySource")
    currency_code: Optional[CurrencyCode] = Field(None, alias="CurrencyCode")
    base: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="Base", description="The price prior to all applicable taxes of a product such as the rate for a room or fare for a flight.")
    taxes: Optional[Taxes] = Field(None, alias="Taxes")
    fees: Optional[Fees] = Field(None, alias="Fees")
    total: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="Total", description="Specifies the total price including base + taxes + fees")
    approximate_ind: Optional[StrictBool] = Field(None, alias="approximateInd", description="True if this amount has been converted from the original amount")
    __properties = ["@type", "currencySource", "CurrencyCode", "Base", "Taxes", "Fees", "Total", "approximateInd"]

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
    def from_json(cls, json_str: str) -> Amount:
        """Create an instance of Amount from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of currency_code
        if self.currency_code:
            _dict['CurrencyCode'] = self.currency_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of taxes
        if self.taxes:
            _dict['Taxes'] = self.taxes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fees
        if self.fees:
            _dict['Fees'] = self.fees.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Amount:
        """Create an instance of Amount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Amount.parse_obj(obj)

        _obj = Amount.parse_obj({
            "type": obj.get("@type"),
            "currency_source": obj.get("currencySource"),
            "currency_code": CurrencyCode.from_dict(obj.get("CurrencyCode")) if obj.get("CurrencyCode") is not None else None,
            "base": obj.get("Base"),
            "taxes": Taxes.from_dict(obj.get("Taxes")) if obj.get("Taxes") is not None else None,
            "fees": Fees.from_dict(obj.get("Fees")) if obj.get("Fees") is not None else None,
            "total": obj.get("Total"),
            "approximate_ind": obj.get("approximateInd")
        })
        return _obj


