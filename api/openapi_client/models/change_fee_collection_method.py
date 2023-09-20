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
from pydantic import BaseModel, Field, StrictBool, constr
from openapi_client.models.change_fee_method_enum import ChangeFeeMethodEnum

class ChangeFeeCollectionMethod(BaseModel):
    """
    ChangeFeeCollectionMethod
    """
    value: Optional[ChangeFeeMethodEnum] = None
    code: constr(strict=True, max_length=32) = Field(..., description="The code value")
    sub_code: Optional[constr(strict=True, max_length=32)] = Field(None, alias="subCode", description="The subcode value")
    description: Optional[constr(strict=True, max_length=128)] = Field(None, description="The description value")
    change_fee_issued_separately_ind: Optional[StrictBool] = Field(None, alias="changeFeeIssuedSeparatelyInd", description="if true, the change fee will be issued as a separate transaction to the residual amount")
    tax_included_in_base_amount_ind: Optional[StrictBool] = Field(None, alias="taxIncludedInBaseAmountInd", description="If true, the tax  on the fee will be included in the base fee amount and sent as a single value to the supplier for fulfilment")
    __properties = ["value", "code", "subCode", "description", "changeFeeIssuedSeparatelyInd", "taxIncludedInBaseAmountInd"]

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
    def from_json(cls, json_str: str) -> ChangeFeeCollectionMethod:
        """Create an instance of ChangeFeeCollectionMethod from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of value
        if self.value:
            _dict['value'] = self.value.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ChangeFeeCollectionMethod:
        """Create an instance of ChangeFeeCollectionMethod from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ChangeFeeCollectionMethod.parse_obj(obj)

        _obj = ChangeFeeCollectionMethod.parse_obj({
            "value": ChangeFeeMethodEnum.from_dict(obj.get("value")) if obj.get("value") is not None else None,
            "code": obj.get("code"),
            "sub_code": obj.get("subCode"),
            "description": obj.get("description"),
            "change_fee_issued_separately_ind": obj.get("changeFeeIssuedSeparatelyInd"),
            "tax_included_in_base_amount_ind": obj.get("taxIncludedInBaseAmountInd")
        })
        return _obj


