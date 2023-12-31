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
from pydantic import Field, constr, validator
from openapi_client.models.agency_info import AgencyInfo
from openapi_client.models.alternate_amount import AlternateAmount
from openapi_client.models.form_of_payment import FormOfPayment
from openapi_client.models.identifier import Identifier
from openapi_client.models.original_issue import OriginalIssue
from openapi_client.models.person_name import PersonName
from openapi_client.models.previous_issue import PreviousIssue
from openapi_client.models.pricing_type_enum import PricingTypeEnum
from openapi_client.models.supplier_locator import SupplierLocator
from openapi_client.models.ticket import Ticket
from openapi_client.models.ticket_price import TicketPrice
from openapi_client.models.ticket_segment import TicketSegment

class TicketDetail(Ticket):
    """
    TicketDetail
    """
    sell_amount: Optional[AlternateAmount] = Field(None, alias="SellAmount")
    pricing_pcc: Optional[constr(strict=True, max_length=10, min_length=2)] = Field(None, alias="PricingPCC")
    __properties = ["@type", "objID", "TicketRef", "Identifier", "numberOfTicketsIssued", "settlementAuthorizationCode", "tourCode", "accountCode", "ticketDesignator", "PersonName", "ReservationLocator", "FormOfPayment", "TicketSegment", "TicketPrice", "PassengerTypeCode", "ValidatingCarrier", "PricingType", "Restrictions", "AgencyInfo", "OriginalIssue", "PreviousIssue", "SellAmount", "PricingPCC"]

    @validator('pricing_pcc')
    def pricing_pcc_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"([a-zA-Z0-9]{2,10})", value):
            raise ValueError(r"must validate the regular expression /([a-zA-Z0-9]{2,10})/")
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
    def from_json(cls, json_str: str) -> TicketDetail:
        """Create an instance of TicketDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of person_name
        if self.person_name:
            _dict['PersonName'] = self.person_name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reservation_locator
        if self.reservation_locator:
            _dict['ReservationLocator'] = self.reservation_locator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in form_of_payment (list)
        _items = []
        if self.form_of_payment:
            for _item in self.form_of_payment:
                if _item:
                    _items.append(_item.to_dict())
            _dict['FormOfPayment'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in ticket_segment (list)
        _items = []
        if self.ticket_segment:
            for _item in self.ticket_segment:
                if _item:
                    _items.append(_item.to_dict())
            _dict['TicketSegment'] = _items
        # override the default output from pydantic by calling `to_dict()` of ticket_price
        if self.ticket_price:
            _dict['TicketPrice'] = self.ticket_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of agency_info
        if self.agency_info:
            _dict['AgencyInfo'] = self.agency_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of original_issue
        if self.original_issue:
            _dict['OriginalIssue'] = self.original_issue.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in previous_issue (list)
        _items = []
        if self.previous_issue:
            for _item in self.previous_issue:
                if _item:
                    _items.append(_item.to_dict())
            _dict['PreviousIssue'] = _items
        # override the default output from pydantic by calling `to_dict()` of sell_amount
        if self.sell_amount:
            _dict['SellAmount'] = self.sell_amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TicketDetail:
        """Create an instance of TicketDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TicketDetail.parse_obj(obj)

        _obj = TicketDetail.parse_obj({
            "type": obj.get("@type"),
            "obj_id": obj.get("objID"),
            "ticket_ref": obj.get("TicketRef"),
            "identifier": Identifier.from_dict(obj.get("Identifier")) if obj.get("Identifier") is not None else None,
            "number_of_tickets_issued": obj.get("numberOfTicketsIssued"),
            "settlement_authorization_code": obj.get("settlementAuthorizationCode"),
            "tour_code": obj.get("tourCode"),
            "account_code": obj.get("accountCode"),
            "ticket_designator": obj.get("ticketDesignator"),
            "person_name": PersonName.from_dict(obj.get("PersonName")) if obj.get("PersonName") is not None else None,
            "reservation_locator": SupplierLocator.from_dict(obj.get("ReservationLocator")) if obj.get("ReservationLocator") is not None else None,
            "form_of_payment": [FormOfPayment.from_dict(_item) for _item in obj.get("FormOfPayment")] if obj.get("FormOfPayment") is not None else None,
            "ticket_segment": [TicketSegment.from_dict(_item) for _item in obj.get("TicketSegment")] if obj.get("TicketSegment") is not None else None,
            "ticket_price": TicketPrice.from_dict(obj.get("TicketPrice")) if obj.get("TicketPrice") is not None else None,
            "passenger_type_code": obj.get("PassengerTypeCode"),
            "validating_carrier": obj.get("ValidatingCarrier"),
            "pricing_type": obj.get("PricingType"),
            "restrictions": obj.get("Restrictions"),
            "agency_info": AgencyInfo.from_dict(obj.get("AgencyInfo")) if obj.get("AgencyInfo") is not None else None,
            "original_issue": OriginalIssue.from_dict(obj.get("OriginalIssue")) if obj.get("OriginalIssue") is not None else None,
            "previous_issue": [PreviousIssue.from_dict(_item) for _item in obj.get("PreviousIssue")] if obj.get("PreviousIssue") is not None else None,
            "sell_amount": AlternateAmount.from_dict(obj.get("SellAmount")) if obj.get("SellAmount") is not None else None,
            "pricing_pcc": obj.get("PricingPCC")
        })
        return _obj


