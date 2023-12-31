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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist
from openapi_client.models.tax_info import TaxInfo

class Taxes(BaseModel):
    """
    Taxes
    """
    type: StrictStr = Field(..., alias="@type")
    total_taxes: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="TotalTaxes", description="A monetary amount, up to 4 decimal places. Decimal place needs to be included.")
    tax_info: Optional[conlist(TaxInfo, max_items=10)] = Field(None, alias="TaxInfo")
    __properties = ["@type", "TotalTaxes", "TaxInfo"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    # JSON field name that stores the object type
    __discriminator_property_name = '@type'

    # discriminator mappings
    __discriminator_value_class_map = {
        'TaxesDetail': 'TaxesDetail'
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
    def from_json(cls, json_str: str) -> Union(TaxesDetail):
        """Create an instance of Taxes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in tax_info (list)
        _items = []
        if self.tax_info:
            for _item in self.tax_info:
                if _item:
                    _items.append(_item.to_dict())
            _dict['TaxInfo'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Union(TaxesDetail):
        """Create an instance of Taxes from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("Taxes failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

from openapi_client.models.taxes_detail import TaxesDetail
Taxes.update_forward_refs()

