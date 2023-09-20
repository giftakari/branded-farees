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
from pydantic import Field, StrictBool, conlist
from openapi_client.models.agency_service_fee_identifier import AgencyServiceFeeIdentifier
from openapi_client.models.currency_amount import CurrencyAmount
from openapi_client.models.extended_payment import ExtendedPayment
from openapi_client.models.fees import Fees
from openapi_client.models.form_of_payment_identifier import FormOfPaymentIdentifier
from openapi_client.models.identifier import Identifier
from openapi_client.models.offer_identifier import OfferIdentifier
from openapi_client.models.payment_id import PaymentID
from openapi_client.models.taxes import Taxes
from openapi_client.models.traveler_identifier_ref import TravelerIdentifierRef

class Payment(PaymentID):
    """
    Payment
    """
    amount: CurrencyAmount = Field(..., alias="Amount")
    form_of_payment_identifier: Optional[FormOfPaymentIdentifier] = Field(None, alias="FormOfPaymentIdentifier")
    offer_identifier: Optional[conlist(OfferIdentifier, max_items=100)] = Field(None, alias="OfferIdentifier")
    fees: Optional[Fees] = Field(None, alias="Fees")
    taxes: Optional[Taxes] = Field(None, alias="Taxes")
    traveler_identifier_ref: Optional[conlist(TravelerIdentifierRef, max_items=100)] = Field(None, alias="TravelerIdentifierRef")
    base_amount: Optional[CurrencyAmount] = Field(None, alias="BaseAmount")
    deposit_ind: Optional[StrictBool] = Field(None, alias="depositInd", description="If true, the payment is a deposit on the referenced Offer")
    extended_payment: Optional[ExtendedPayment] = Field(None, alias="ExtendedPayment")
    agency_service_fee_identifier: Optional[conlist(AgencyServiceFeeIdentifier, max_items=100)] = Field(None, alias="AgencyServiceFeeIdentifier")
    guarantee_ind: Optional[StrictBool] = Field(None, alias="guaranteeInd", description="If true, the payment is a guarantee for the referenced Offer")
    __properties = ["@type", "id", "PaymentRef", "Identifier", "Amount", "FormOfPaymentIdentifier", "OfferIdentifier", "Fees", "Taxes", "TravelerIdentifierRef", "BaseAmount", "depositInd", "ExtendedPayment", "AgencyServiceFeeIdentifier", "guaranteeInd"]

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
    def from_json(cls, json_str: str) -> Payment:
        """Create an instance of Payment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of amount
        if self.amount:
            _dict['Amount'] = self.amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of form_of_payment_identifier
        if self.form_of_payment_identifier:
            _dict['FormOfPaymentIdentifier'] = self.form_of_payment_identifier.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in offer_identifier (list)
        _items = []
        if self.offer_identifier:
            for _item in self.offer_identifier:
                if _item:
                    _items.append(_item.to_dict())
            _dict['OfferIdentifier'] = _items
        # override the default output from pydantic by calling `to_dict()` of fees
        if self.fees:
            _dict['Fees'] = self.fees.to_dict()
        # override the default output from pydantic by calling `to_dict()` of taxes
        if self.taxes:
            _dict['Taxes'] = self.taxes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in traveler_identifier_ref (list)
        _items = []
        if self.traveler_identifier_ref:
            for _item in self.traveler_identifier_ref:
                if _item:
                    _items.append(_item.to_dict())
            _dict['TravelerIdentifierRef'] = _items
        # override the default output from pydantic by calling `to_dict()` of base_amount
        if self.base_amount:
            _dict['BaseAmount'] = self.base_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of extended_payment
        if self.extended_payment:
            _dict['ExtendedPayment'] = self.extended_payment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in agency_service_fee_identifier (list)
        _items = []
        if self.agency_service_fee_identifier:
            for _item in self.agency_service_fee_identifier:
                if _item:
                    _items.append(_item.to_dict())
            _dict['AgencyServiceFeeIdentifier'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Payment:
        """Create an instance of Payment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Payment.parse_obj(obj)

        _obj = Payment.parse_obj({
            "type": obj.get("@type"),
            "id": obj.get("id"),
            "payment_ref": obj.get("PaymentRef"),
            "identifier": Identifier.from_dict(obj.get("Identifier")) if obj.get("Identifier") is not None else None,
            "amount": CurrencyAmount.from_dict(obj.get("Amount")) if obj.get("Amount") is not None else None,
            "form_of_payment_identifier": FormOfPaymentIdentifier.from_dict(obj.get("FormOfPaymentIdentifier")) if obj.get("FormOfPaymentIdentifier") is not None else None,
            "offer_identifier": [OfferIdentifier.from_dict(_item) for _item in obj.get("OfferIdentifier")] if obj.get("OfferIdentifier") is not None else None,
            "fees": Fees.from_dict(obj.get("Fees")) if obj.get("Fees") is not None else None,
            "taxes": Taxes.from_dict(obj.get("Taxes")) if obj.get("Taxes") is not None else None,
            "traveler_identifier_ref": [TravelerIdentifierRef.from_dict(_item) for _item in obj.get("TravelerIdentifierRef")] if obj.get("TravelerIdentifierRef") is not None else None,
            "base_amount": CurrencyAmount.from_dict(obj.get("BaseAmount")) if obj.get("BaseAmount") is not None else None,
            "deposit_ind": obj.get("depositInd"),
            "extended_payment": ExtendedPayment.from_dict(obj.get("ExtendedPayment")) if obj.get("ExtendedPayment") is not None else None,
            "agency_service_fee_identifier": [AgencyServiceFeeIdentifier.from_dict(_item) for _item in obj.get("AgencyServiceFeeIdentifier")] if obj.get("AgencyServiceFeeIdentifier") is not None else None,
            "guarantee_ind": obj.get("guaranteeInd")
        })
        return _obj


