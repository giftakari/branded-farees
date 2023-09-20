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
from pydantic import Field, StrictStr, conlist
from openapi_client.models.accepted_credit_card import AcceptedCreditCard
from openapi_client.models.cancel_penalty import CancelPenalty
from openapi_client.models.check_in_out_policy import CheckInOutPolicy
from openapi_client.models.customer_loyalty import CustomerLoyalty
from openapi_client.models.deposit_policy import DepositPolicy
from openapi_client.models.guarantee import Guarantee
from openapi_client.models.identifier import Identifier
from openapi_client.models.meals_included import MealsIncluded
from openapi_client.models.product_rate_code_info import ProductRateCodeInfo
from openapi_client.models.rate_payment_enum import RatePaymentEnum
from openapi_client.models.terms_and_conditions_full import TermsAndConditionsFull
from openapi_client.models.text_block import TextBlock

class TermsAndConditionsFullHospitality(TermsAndConditionsFull):
    """
    TermsAndConditionsFullHospitality
    """
    guarantee: Optional[conlist(Guarantee, max_items=5)] = Field(None, alias="Guarantee")
    cancel_penalty: Optional[conlist(CancelPenalty, max_items=10)] = Field(None, alias="CancelPenalty")
    accepted_credit_card: Optional[conlist(AcceptedCreditCard, max_items=100)] = Field(None, alias="AcceptedCreditCard")
    description: Optional[conlist(StrictStr, max_items=5)] = Field(None, alias="Description")
    meals_included: Optional[MealsIncluded] = Field(None, alias="MealsIncluded")
    product_rate_code_info: Optional[conlist(ProductRateCodeInfo, max_items=10)] = Field(None, alias="ProductRateCodeInfo")
    check_in_out_policy: Optional[CheckInOutPolicy] = Field(None, alias="CheckInOutPolicy")
    deposit_policy: Optional[DepositPolicy] = Field(None, alias="DepositPolicy")
    rate_payment_info: Optional[RatePaymentEnum] = Field(None, alias="RatePaymentInfo")
    __properties = ["@type", "id", "termsAndConditionsRef", "Identifier", "ExpiryDate", "CustomerLoyalty", "TextBlock", "Guarantee", "CancelPenalty", "AcceptedCreditCard", "Description", "MealsIncluded", "ProductRateCodeInfo", "CheckInOutPolicy", "DepositPolicy", "RatePaymentInfo"]

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
    def from_json(cls, json_str: str) -> TermsAndConditionsFullHospitality:
        """Create an instance of TermsAndConditionsFullHospitality from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of identifier
        if self.identifier:
            _dict['Identifier'] = self.identifier.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in customer_loyalty (list)
        _items = []
        if self.customer_loyalty:
            for _item in self.customer_loyalty:
                if _item:
                    _items.append(_item.to_dict())
            _dict['CustomerLoyalty'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in text_block (list)
        _items = []
        if self.text_block:
            for _item in self.text_block:
                if _item:
                    _items.append(_item.to_dict())
            _dict['TextBlock'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in guarantee (list)
        _items = []
        if self.guarantee:
            for _item in self.guarantee:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Guarantee'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in cancel_penalty (list)
        _items = []
        if self.cancel_penalty:
            for _item in self.cancel_penalty:
                if _item:
                    _items.append(_item.to_dict())
            _dict['CancelPenalty'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in accepted_credit_card (list)
        _items = []
        if self.accepted_credit_card:
            for _item in self.accepted_credit_card:
                if _item:
                    _items.append(_item.to_dict())
            _dict['AcceptedCreditCard'] = _items
        # override the default output from pydantic by calling `to_dict()` of meals_included
        if self.meals_included:
            _dict['MealsIncluded'] = self.meals_included.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in product_rate_code_info (list)
        _items = []
        if self.product_rate_code_info:
            for _item in self.product_rate_code_info:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ProductRateCodeInfo'] = _items
        # override the default output from pydantic by calling `to_dict()` of check_in_out_policy
        if self.check_in_out_policy:
            _dict['CheckInOutPolicy'] = self.check_in_out_policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of deposit_policy
        if self.deposit_policy:
            _dict['DepositPolicy'] = self.deposit_policy.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TermsAndConditionsFullHospitality:
        """Create an instance of TermsAndConditionsFullHospitality from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TermsAndConditionsFullHospitality.parse_obj(obj)

        _obj = TermsAndConditionsFullHospitality.parse_obj({
            "type": obj.get("@type"),
            "id": obj.get("id"),
            "terms_and_conditions_ref": obj.get("termsAndConditionsRef"),
            "identifier": Identifier.from_dict(obj.get("Identifier")) if obj.get("Identifier") is not None else None,
            "expiry_date": obj.get("ExpiryDate"),
            "customer_loyalty": [CustomerLoyalty.from_dict(_item) for _item in obj.get("CustomerLoyalty")] if obj.get("CustomerLoyalty") is not None else None,
            "text_block": [TextBlock.from_dict(_item) for _item in obj.get("TextBlock")] if obj.get("TextBlock") is not None else None,
            "guarantee": [Guarantee.from_dict(_item) for _item in obj.get("Guarantee")] if obj.get("Guarantee") is not None else None,
            "cancel_penalty": [CancelPenalty.from_dict(_item) for _item in obj.get("CancelPenalty")] if obj.get("CancelPenalty") is not None else None,
            "accepted_credit_card": [AcceptedCreditCard.from_dict(_item) for _item in obj.get("AcceptedCreditCard")] if obj.get("AcceptedCreditCard") is not None else None,
            "description": obj.get("Description"),
            "meals_included": MealsIncluded.from_dict(obj.get("MealsIncluded")) if obj.get("MealsIncluded") is not None else None,
            "product_rate_code_info": [ProductRateCodeInfo.from_dict(_item) for _item in obj.get("ProductRateCodeInfo")] if obj.get("ProductRateCodeInfo") is not None else None,
            "check_in_out_policy": CheckInOutPolicy.from_dict(obj.get("CheckInOutPolicy")) if obj.get("CheckInOutPolicy") is not None else None,
            "deposit_policy": DepositPolicy.from_dict(obj.get("DepositPolicy")) if obj.get("DepositPolicy") is not None else None,
            "rate_payment_info": obj.get("RatePaymentInfo")
        })
        return _obj

