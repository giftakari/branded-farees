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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, constr, validator
from openapi_client.models.brand_inclusion_enum import BrandInclusionEnum

class AdditionalBrandAttribute(BaseModel):
    """
    AdditionalBrandAttribute
    """
    type: StrictStr = Field(..., alias="@type")
    classification: constr(strict=True, max_length=512) = Field(..., alias="Classification", description="The Travelport classification used for categories of ancillaries")
    inclusion: BrandInclusionEnum = Field(..., alias="Inclusion")
    image_url: Optional[conlist(StrictStr, max_items=10)] = Field(None, alias="ImageURL")
    matched_attribute_ind: Optional[StrictBool] = Field(None, alias="matchedAttributeInd", description="If true, this is a matched attribute")
    group_code: Optional[constr(strict=True, max_length=10)] = Field(None, alias="groupCode")
    sub_group_code: Optional[constr(strict=True, max_length=10)] = Field(None, alias="subGroupCode")
    sub_code: Optional[constr(strict=True, max_length=10)] = Field(None, alias="subCode")
    __properties = ["@type", "Classification", "Inclusion", "ImageURL", "matchedAttributeInd", "groupCode", "subGroupCode", "subCode"]

    @validator('group_code')
    def group_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"([A-Z0-9]+)?", value):
            raise ValueError(r"must validate the regular expression /([A-Z0-9]+)?/")
        return value

    @validator('sub_group_code')
    def sub_group_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"([A-Z0-9]+)?", value):
            raise ValueError(r"must validate the regular expression /([A-Z0-9]+)?/")
        return value

    @validator('sub_code')
    def sub_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"([A-Z0-9]+)?", value):
            raise ValueError(r"must validate the regular expression /([A-Z0-9]+)?/")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    # JSON field name that stores the object type
    __discriminator_property_name = '@type'

    # discriminator mappings
    __discriminator_value_class_map = {
        'AdditionalBrandAttributeCompleteInfo': 'AdditionalBrandAttributeCompleteInfo'
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
    def from_json(cls, json_str: str) -> Union(AdditionalBrandAttributeCompleteInfo):
        """Create an instance of AdditionalBrandAttribute from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Union(AdditionalBrandAttributeCompleteInfo):
        """Create an instance of AdditionalBrandAttribute from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("AdditionalBrandAttribute failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

from openapi_client.models.additional_brand_attribute_complete_info import AdditionalBrandAttributeCompleteInfo
AdditionalBrandAttribute.update_forward_refs()

