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
from pydantic import BaseModel, Field, constr, validator

class RailDiscountCard(BaseModel):
    """
    The name of the Rail Discount
    """
    value: Optional[constr(strict=True, max_length=128)] = None
    supplier_code: constr(strict=True, max_length=5, min_length=2) = Field(..., alias="supplierCode", description="Code of the Supplier")
    reference_number: Optional[constr(strict=True, max_length=128)] = Field(None, alias="referenceNumber", description="ReferenceNumber")
    __properties = ["value", "supplierCode", "referenceNumber"]

    @validator('supplier_code')
    def supplier_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"([a-zA-Z0-9]{2,5})", value):
            raise ValueError(r"must validate the regular expression /([a-zA-Z0-9]{2,5})/")
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
    def from_json(cls, json_str: str) -> RailDiscountCard:
        """Create an instance of RailDiscountCard from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RailDiscountCard:
        """Create an instance of RailDiscountCard from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RailDiscountCard.parse_obj(obj)

        _obj = RailDiscountCard.parse_obj({
            "value": obj.get("value"),
            "supplier_code": obj.get("supplierCode"),
            "reference_number": obj.get("referenceNumber")
        })
        return _obj


