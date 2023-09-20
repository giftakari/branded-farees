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
from pydantic import BaseModel, Field, StrictStr, conlist
from openapi_client.models.currency_rate_conversion import CurrencyRateConversion
from openapi_client.models.identifier import Identifier
from openapi_client.models.next_steps import NextSteps
from openapi_client.models.reference_list import ReferenceList
from openapi_client.models.result import Result
from openapi_client.models.special_service_id import SpecialServiceID

class SpecialServiceListResponse(BaseModel):
    """
    SpecialServiceListResponse
    """
    type: Optional[StrictStr] = Field(None, alias="@type")
    special_service_id: Optional[conlist(SpecialServiceID)] = Field(None, alias="SpecialServiceID")
    transaction_id: Optional[StrictStr] = Field(None, alias="transactionId", description="Unique transaction, correlation or tracking id for a single request and reply i.e. for a single transaction. Should be a 128 bit GUID format. Also know as E2ETrackingId.")
    trace_id: Optional[StrictStr] = Field(None, alias="traceId", description="Optional ID for internal child transactions created for processing a single request (single transaction). Should be a 128 bit GUID format. Also known as ChildTrackingId.")
    result: Optional[Result] = Field(None, alias="Result")
    identifier: Optional[Identifier] = Field(None, alias="Identifier")
    next_steps: Optional[NextSteps] = Field(None, alias="NextSteps")
    reference_list: Optional[conlist(ReferenceList, max_items=5)] = Field(None, alias="ReferenceList")
    currency_rate_conversion: Optional[conlist(CurrencyRateConversion, max_items=5)] = Field(None, alias="CurrencyRateConversion")
    __properties = ["transactionId", "traceId", "Result", "Identifier", "NextSteps", "ReferenceList", "CurrencyRateConversion"]

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
    def from_json(cls, json_str: str) -> SpecialServiceListResponse:
        """Create an instance of SpecialServiceListResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of result
        if self.result:
            _dict['Result'] = self.result.to_dict()
        # override the default output from pydantic by calling `to_dict()` of identifier
        if self.identifier:
            _dict['Identifier'] = self.identifier.to_dict()
        # override the default output from pydantic by calling `to_dict()` of next_steps
        if self.next_steps:
            _dict['NextSteps'] = self.next_steps.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in reference_list (list)
        _items = []
        if self.reference_list:
            for _item in self.reference_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ReferenceList'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in currency_rate_conversion (list)
        _items = []
        if self.currency_rate_conversion:
            for _item in self.currency_rate_conversion:
                if _item:
                    _items.append(_item.to_dict())
            _dict['CurrencyRateConversion'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SpecialServiceListResponse:
        """Create an instance of SpecialServiceListResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SpecialServiceListResponse.parse_obj(obj)

        _obj = SpecialServiceListResponse.parse_obj({
            "transaction_id": obj.get("transactionId"),
            "trace_id": obj.get("traceId"),
            "result": Result.from_dict(obj.get("Result")) if obj.get("Result") is not None else None,
            "identifier": Identifier.from_dict(obj.get("Identifier")) if obj.get("Identifier") is not None else None,
            "next_steps": NextSteps.from_dict(obj.get("NextSteps")) if obj.get("NextSteps") is not None else None,
            "reference_list": [ReferenceList.from_dict(_item) for _item in obj.get("ReferenceList")] if obj.get("ReferenceList") is not None else None,
            "currency_rate_conversion": [CurrencyRateConversion.from_dict(_item) for _item in obj.get("CurrencyRateConversion")] if obj.get("CurrencyRateConversion") is not None else None
        })
        return _obj


