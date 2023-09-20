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
from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.change_options import ChangeOptions
from openapi_client.models.fare_qualifier_enum import FareQualifierENUM
from openapi_client.models.fares_filter_enum import FaresFilterEnum
from openapi_client.models.refund_options import RefundOptions

class FareSelection(BaseModel):
    """
    FareSelection
    """
    type: StrictStr = Field(..., alias="@type")
    fare_type: Optional[FaresFilterEnum] = Field(None, alias="fareType")
    refund_options: Optional[RefundOptions] = Field(None, alias="RefundOptions")
    change_options: Optional[ChangeOptions] = Field(None, alias="ChangeOptions")
    fare_qualifier: Optional[FareQualifierENUM] = Field(None, alias="FareQualifier")
    __properties = ["@type", "fareType", "RefundOptions", "ChangeOptions", "FareQualifier"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    # JSON field name that stores the object type
    __discriminator_property_name = '@type'

    # discriminator mappings
    __discriminator_value_class_map = {
        'FareSelectionDetail': 'FareSelectionDetail'
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
    def from_json(cls, json_str: str) -> Union(FareSelectionDetail):
        """Create an instance of FareSelection from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of refund_options
        if self.refund_options:
            _dict['RefundOptions'] = self.refund_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of change_options
        if self.change_options:
            _dict['ChangeOptions'] = self.change_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fare_qualifier
        if self.fare_qualifier:
            _dict['FareQualifier'] = self.fare_qualifier.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Union(FareSelectionDetail):
        """Create an instance of FareSelection from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("FareSelection failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

from openapi_client.models.fare_selection_detail import FareSelectionDetail
FareSelection.update_forward_refs()

