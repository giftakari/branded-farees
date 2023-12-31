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
from pydantic import BaseModel, Field, StrictStr, constr, validator
from openapi_client.models.currency_amount import CurrencyAmount
from openapi_client.models.text_title_and_description import TextTitleAndDescription

class AdditionalDetail(BaseModel):
    """
    AdditionalDetail
    """
    type: Optional[StrictStr] = Field(None, alias="@type")
    detail_type: Optional[constr(strict=True)] = Field(None, alias="detailType", description="OTA Code")
    code: Optional[constr(strict=True, max_length=32)] = Field(None, description="Partner code")
    amount: Optional[CurrencyAmount] = Field(None, alias="Amount")
    description: Optional[TextTitleAndDescription] = Field(None, alias="Description")
    __properties = ["@type", "detailType", "code", "Amount", "Description"]

    @validator('detail_type')
    def detail_type_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[0-9A-Z]{1,3}(\.[A-Z]{3}(\.X){0,1}){0,1}", value):
            raise ValueError(r"must validate the regular expression /[0-9A-Z]{1,3}(\.[A-Z]{3}(\.X){0,1}){0,1}/")
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
    def from_json(cls, json_str: str) -> AdditionalDetail:
        """Create an instance of AdditionalDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of amount
        if self.amount:
            _dict['Amount'] = self.amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of description
        if self.description:
            _dict['Description'] = self.description.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AdditionalDetail:
        """Create an instance of AdditionalDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AdditionalDetail.parse_obj(obj)

        _obj = AdditionalDetail.parse_obj({
            "type": obj.get("@type"),
            "detail_type": obj.get("detailType"),
            "code": obj.get("code"),
            "amount": CurrencyAmount.from_dict(obj.get("Amount")) if obj.get("Amount") is not None else None,
            "description": TextTitleAndDescription.from_dict(obj.get("Description")) if obj.get("Description") is not None else None
        })
        return _obj


