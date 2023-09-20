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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, constr
from openapi_client.models.application_enum import ApplicationEnum
from openapi_client.models.fee_amount_or_percent import FeeAmountOrPercent
from openapi_client.models.frequency_enum import FrequencyEnum
from openapi_client.models.tax import Tax

class Fee(BaseModel):
    """
    Fee
    """
    type: Optional[StrictStr] = Field(None, alias="@type")
    fee_code: Optional[constr(strict=True, max_length=32)] = Field(None, alias="feeCode", description="Fee code")
    reporting_authority: Optional[constr(strict=True, max_length=32)] = Field(None, alias="reportingAuthority", description="Identifies the reporting authority.")
    purpose: Optional[constr(strict=True, max_length=32)] = Field(None, description="Fee purpose")
    description: Optional[constr(strict=True, max_length=512)] = Field(None, description="Fee description")
    fee_application: Optional[ApplicationEnum] = Field(None, alias="feeApplication")
    fee_frequency: Optional[FrequencyEnum] = Field(None, alias="feeFrequency")
    fee_amount_or_percent: FeeAmountOrPercent = Field(..., alias="FeeAmountOrPercent")
    tax: Optional[conlist(Tax, max_items=5)] = Field(None, alias="Tax")
    includedin_base_ind: Optional[StrictBool] = Field(None, alias="includedinBaseInd", description="If the fee is included in the Base Price")
    __properties = ["@type", "feeCode", "reportingAuthority", "purpose", "description", "feeApplication", "feeFrequency", "FeeAmountOrPercent", "Tax", "includedinBaseInd"]

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
    def from_json(cls, json_str: str) -> Fee:
        """Create an instance of Fee from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of fee_amount_or_percent
        if self.fee_amount_or_percent:
            _dict['FeeAmountOrPercent'] = self.fee_amount_or_percent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in tax (list)
        _items = []
        if self.tax:
            for _item in self.tax:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Tax'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Fee:
        """Create an instance of Fee from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Fee.parse_obj(obj)

        _obj = Fee.parse_obj({
            "type": obj.get("@type"),
            "fee_code": obj.get("feeCode"),
            "reporting_authority": obj.get("reportingAuthority"),
            "purpose": obj.get("purpose"),
            "description": obj.get("description"),
            "fee_application": obj.get("feeApplication"),
            "fee_frequency": obj.get("feeFrequency"),
            "fee_amount_or_percent": FeeAmountOrPercent.from_dict(obj.get("FeeAmountOrPercent")) if obj.get("FeeAmountOrPercent") is not None else None,
            "tax": [Tax.from_dict(_item) for _item in obj.get("Tax")] if obj.get("Tax") is not None else None,
            "includedin_base_ind": obj.get("includedinBaseInd")
        })
        return _obj

