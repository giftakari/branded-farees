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
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from openapi_client.models.currency_code import CurrencyCode
from openapi_client.models.vendor_currency_total import VendorCurrencyTotal

class Price(BaseModel):
    """
    Price
    """
    type: StrictStr = Field(..., alias="@type")
    id: Optional[StrictStr] = Field(None, description="Internally referenced id")
    currency_code: Optional[CurrencyCode] = Field(None, alias="CurrencyCode")
    base: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="Base", description="The total amount not including taxes and/or fees")
    total_taxes: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="TotalTaxes", description="The total of the taxes included in the total price")
    total_fees: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="TotalFees", description="The total of the fees included in the total price")
    total_price: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="TotalPrice", description="The total price of the product in the currency indicated")
    vendor_currency_total: Optional[VendorCurrencyTotal] = Field(None, alias="VendorCurrencyTotal")
    __properties = ["@type", "id", "CurrencyCode", "Base", "TotalTaxes", "TotalFees", "TotalPrice", "VendorCurrencyTotal"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    # JSON field name that stores the object type
    __discriminator_property_name = '@type'

    # discriminator mappings
    __discriminator_value_class_map = {
        'PriceDetail': 'PriceDetail'
    }

    @classmethod
    def get_discriminator_value(cls, obj: dict) -> str:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Union(PriceDetail):
        """Create an instance of Price from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of vendor_currency_total
        if self.vendor_currency_total:
            _dict['VendorCurrencyTotal'] = self.vendor_currency_total.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Union(PriceDetail):
        """Create an instance of Price from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("Price failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

from openapi_client.models.price_detail import PriceDetail
Price.update_forward_refs()

