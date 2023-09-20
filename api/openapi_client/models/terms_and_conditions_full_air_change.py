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
from pydantic import Field, conlist
from openapi_client.models.baggage_allowance import BaggageAllowance
from openapi_client.models.baggage_recheck import BaggageRecheck
from openapi_client.models.customer_loyalty import CustomerLoyalty
from openapi_client.models.document_valid_date_range import DocumentValidDateRange
from openapi_client.models.fare_guarantee_policy import FareGuaranteePolicy
from openapi_client.models.fulfillment_method import FulfillmentMethod
from openapi_client.models.identifier import Identifier
from openapi_client.models.identifier_ref import IdentifierRef
from openapi_client.models.organization_information import OrganizationInformation
from openapi_client.models.penalties import Penalties
from openapi_client.models.pricing_agency import PricingAgency
from openapi_client.models.promotional_code import PromotionalCode
from openapi_client.models.restriction import Restriction
from openapi_client.models.terms_and_conditions_full_air import TermsAndConditionsFullAir
from openapi_client.models.text_block import TextBlock
from openapi_client.models.ticketing_agency import TicketingAgency
from openapi_client.models.tour_codes import TourCodes
from openapi_client.models.validating_airline import ValidatingAirline

class TermsAndConditionsFullAirChange(TermsAndConditionsFullAir):
    """
    TermsAndConditionsFullAirChange
    """
    fulfillment_method: Optional[conlist(FulfillmentMethod, max_items=10)] = Field(None, alias="FulfillmentMethod")
    __properties = ["@type", "id", "termsAndConditionsRef", "Identifier", "ExpiryDate", "CustomerLoyalty", "TextBlock", "BaggageAllowance", "FareRuleIdentifierRef", "Restriction", "OrganizationInformation", "ValidatingAirline", "BaggageRecheck", "TicketingAgency", "PaymentTimeLimit", "PromotionalCode", "Penalties", "FareGuaranteePolicy", "PricingAgency", "instantPurchaseInd", "secureFlightPassengerDataRequiredInd", "TourCodes", "DocumentValidDateRange", "FulfillmentMethod"]

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
    def from_json(cls, json_str: str) -> TermsAndConditionsFullAirChange:
        """Create an instance of TermsAndConditionsFullAirChange from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in baggage_allowance (list)
        _items = []
        if self.baggage_allowance:
            for _item in self.baggage_allowance:
                if _item:
                    _items.append(_item.to_dict())
            _dict['BaggageAllowance'] = _items
        # override the default output from pydantic by calling `to_dict()` of fare_rule_identifier_ref
        if self.fare_rule_identifier_ref:
            _dict['FareRuleIdentifierRef'] = self.fare_rule_identifier_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in restriction (list)
        _items = []
        if self.restriction:
            for _item in self.restriction:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Restriction'] = _items
        # override the default output from pydantic by calling `to_dict()` of organization_information
        if self.organization_information:
            _dict['OrganizationInformation'] = self.organization_information.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in validating_airline (list)
        _items = []
        if self.validating_airline:
            for _item in self.validating_airline:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ValidatingAirline'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in baggage_recheck (list)
        _items = []
        if self.baggage_recheck:
            for _item in self.baggage_recheck:
                if _item:
                    _items.append(_item.to_dict())
            _dict['BaggageRecheck'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in ticketing_agency (list)
        _items = []
        if self.ticketing_agency:
            for _item in self.ticketing_agency:
                if _item:
                    _items.append(_item.to_dict())
            _dict['TicketingAgency'] = _items
        # override the default output from pydantic by calling `to_dict()` of promotional_code
        if self.promotional_code:
            _dict['PromotionalCode'] = self.promotional_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in penalties (list)
        _items = []
        if self.penalties:
            for _item in self.penalties:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Penalties'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in fare_guarantee_policy (list)
        _items = []
        if self.fare_guarantee_policy:
            for _item in self.fare_guarantee_policy:
                if _item:
                    _items.append(_item.to_dict())
            _dict['FareGuaranteePolicy'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in pricing_agency (list)
        _items = []
        if self.pricing_agency:
            for _item in self.pricing_agency:
                if _item:
                    _items.append(_item.to_dict())
            _dict['PricingAgency'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in tour_codes (list)
        _items = []
        if self.tour_codes:
            for _item in self.tour_codes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['TourCodes'] = _items
        # override the default output from pydantic by calling `to_dict()` of document_valid_date_range
        if self.document_valid_date_range:
            _dict['DocumentValidDateRange'] = self.document_valid_date_range.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in fulfillment_method (list)
        _items = []
        if self.fulfillment_method:
            for _item in self.fulfillment_method:
                if _item:
                    _items.append(_item.to_dict())
            _dict['FulfillmentMethod'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TermsAndConditionsFullAirChange:
        """Create an instance of TermsAndConditionsFullAirChange from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TermsAndConditionsFullAirChange.parse_obj(obj)

        _obj = TermsAndConditionsFullAirChange.parse_obj({
            "type": obj.get("@type"),
            "id": obj.get("id"),
            "terms_and_conditions_ref": obj.get("termsAndConditionsRef"),
            "identifier": Identifier.from_dict(obj.get("Identifier")) if obj.get("Identifier") is not None else None,
            "expiry_date": obj.get("ExpiryDate"),
            "customer_loyalty": [CustomerLoyalty.from_dict(_item) for _item in obj.get("CustomerLoyalty")] if obj.get("CustomerLoyalty") is not None else None,
            "text_block": [TextBlock.from_dict(_item) for _item in obj.get("TextBlock")] if obj.get("TextBlock") is not None else None,
            "baggage_allowance": [BaggageAllowance.from_dict(_item) for _item in obj.get("BaggageAllowance")] if obj.get("BaggageAllowance") is not None else None,
            "fare_rule_identifier_ref": IdentifierRef.from_dict(obj.get("FareRuleIdentifierRef")) if obj.get("FareRuleIdentifierRef") is not None else None,
            "restriction": [Restriction.from_dict(_item) for _item in obj.get("Restriction")] if obj.get("Restriction") is not None else None,
            "organization_information": OrganizationInformation.from_dict(obj.get("OrganizationInformation")) if obj.get("OrganizationInformation") is not None else None,
            "validating_airline": [ValidatingAirline.from_dict(_item) for _item in obj.get("ValidatingAirline")] if obj.get("ValidatingAirline") is not None else None,
            "baggage_recheck": [BaggageRecheck.from_dict(_item) for _item in obj.get("BaggageRecheck")] if obj.get("BaggageRecheck") is not None else None,
            "ticketing_agency": [TicketingAgency.from_dict(_item) for _item in obj.get("TicketingAgency")] if obj.get("TicketingAgency") is not None else None,
            "payment_time_limit": obj.get("PaymentTimeLimit"),
            "promotional_code": PromotionalCode.from_dict(obj.get("PromotionalCode")) if obj.get("PromotionalCode") is not None else None,
            "penalties": [Penalties.from_dict(_item) for _item in obj.get("Penalties")] if obj.get("Penalties") is not None else None,
            "fare_guarantee_policy": [FareGuaranteePolicy.from_dict(_item) for _item in obj.get("FareGuaranteePolicy")] if obj.get("FareGuaranteePolicy") is not None else None,
            "pricing_agency": [PricingAgency.from_dict(_item) for _item in obj.get("PricingAgency")] if obj.get("PricingAgency") is not None else None,
            "instant_purchase_ind": obj.get("instantPurchaseInd"),
            "secure_flight_passenger_data_required_ind": obj.get("secureFlightPassengerDataRequiredInd"),
            "tour_codes": [TourCodes.from_dict(_item) for _item in obj.get("TourCodes")] if obj.get("TourCodes") is not None else None,
            "document_valid_date_range": DocumentValidDateRange.from_dict(obj.get("DocumentValidDateRange")) if obj.get("DocumentValidDateRange") is not None else None,
            "fulfillment_method": [FulfillmentMethod.from_dict(_item) for _item in obj.get("FulfillmentMethod")] if obj.get("FulfillmentMethod") is not None else None
        })
        return _obj

