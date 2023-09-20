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
from pydantic import BaseModel, Field, conlist, constr, validator
from openapi_client.models.filed_amount import FiledAmount
from openapi_client.models.net_fare_breakdown_construction import NetFareBreakdownConstruction
from openapi_client.models.ticket_base_passenger import TicketBasePassenger

class NetFareInfo(BaseModel):
    """
    NetFareInfo
    """
    passenger_type_code: Optional[constr(strict=True, max_length=5, min_length=3)] = Field(None, alias="passengerTypeCode", description="PassengerTypeCode")
    net_fare_breakdown_construction: Optional[conlist(NetFareBreakdownConstruction, max_items=10)] = Field(None, alias="NetFareBreakdownConstruction")
    ticket_base_audit: Optional[FiledAmount] = Field(None, alias="TicketBaseAudit")
    ticket_base_passenger: Optional[TicketBasePassenger] = Field(None, alias="TicketBasePassenger")
    __properties = ["passengerTypeCode", "NetFareBreakdownConstruction", "TicketBaseAudit", "TicketBasePassenger"]

    @validator('passenger_type_code')
    def passenger_type_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"([a-zA-Z0-9]{3,5})", value):
            raise ValueError(r"must validate the regular expression /([a-zA-Z0-9]{3,5})/")
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
    def from_json(cls, json_str: str) -> NetFareInfo:
        """Create an instance of NetFareInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in net_fare_breakdown_construction (list)
        _items = []
        if self.net_fare_breakdown_construction:
            for _item in self.net_fare_breakdown_construction:
                if _item:
                    _items.append(_item.to_dict())
            _dict['NetFareBreakdownConstruction'] = _items
        # override the default output from pydantic by calling `to_dict()` of ticket_base_audit
        if self.ticket_base_audit:
            _dict['TicketBaseAudit'] = self.ticket_base_audit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ticket_base_passenger
        if self.ticket_base_passenger:
            _dict['TicketBasePassenger'] = self.ticket_base_passenger.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NetFareInfo:
        """Create an instance of NetFareInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NetFareInfo.parse_obj(obj)

        _obj = NetFareInfo.parse_obj({
            "passenger_type_code": obj.get("passengerTypeCode"),
            "net_fare_breakdown_construction": [NetFareBreakdownConstruction.from_dict(_item) for _item in obj.get("NetFareBreakdownConstruction")] if obj.get("NetFareBreakdownConstruction") is not None else None,
            "ticket_base_audit": FiledAmount.from_dict(obj.get("TicketBaseAudit")) if obj.get("TicketBaseAudit") is not None else None,
            "ticket_base_passenger": TicketBasePassenger.from_dict(obj.get("TicketBasePassenger")) if obj.get("TicketBasePassenger") is not None else None
        })
        return _obj

