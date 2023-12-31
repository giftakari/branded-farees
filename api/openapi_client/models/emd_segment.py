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
from pydantic import BaseModel, Field, StrictInt, StrictStr, constr, validator
from openapi_client.models.amount import Amount
from openapi_client.models.emd_description import EMDDescription
from openapi_client.models.emd_status_enum import EMDStatusENUM

class EMDSegment(BaseModel):
    """
    EMDSegment
    """
    type: Optional[StrictStr] = Field(None, alias="@type")
    sequence: StrictInt = Field(..., description="Sequence of EMDSegment")
    quantity: Optional[StrictInt] = Field(None, description="The quantity of the ancillary available on this EMDSegment")
    emd_description: Optional[EMDDescription] = Field(None, alias="EMDDescription")
    amount: Optional[Amount] = Field(None, alias="Amount")
    status: Optional[EMDStatusENUM] = Field(None, alias="Status")
    date_of_service: Optional[constr(strict=True)] = Field(None, alias="DateOfService", description="The date of service the service is available for")
    present_to: Optional[constr(strict=True)] = Field(None, alias="PresentTo", description="The airline the EMD should be presented to to supply the service")
    present_at: Optional[constr(strict=True, max_length=3, min_length=3)] = Field(None, alias="PresentAt", description="The location the EMD should be presented to to supply the service")
    routing: Optional[constr(strict=True, max_length=128)] = Field(None, alias="Routing", description="The routing the service is valid on")
    __properties = ["@type", "sequence", "quantity", "EMDDescription", "Amount", "Status", "DateOfService", "PresentTo", "PresentAt", "Routing"]

    @validator('date_of_service')
    def date_of_service_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"(\d{4}-\d{2}-\d{2})", value):
            raise ValueError(r"must validate the regular expression /(\d{4}-\d{2}-\d{2})/")
        return value

    @validator('present_to')
    def present_to_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"([a-zA-Z0-9]{2,3})", value):
            raise ValueError(r"must validate the regular expression /([a-zA-Z0-9]{2,3})/")
        return value

    @validator('present_at')
    def present_at_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"([a-zA-Z]{3})", value):
            raise ValueError(r"must validate the regular expression /([a-zA-Z]{3})/")
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
    def from_json(cls, json_str: str) -> EMDSegment:
        """Create an instance of EMDSegment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of emd_description
        if self.emd_description:
            _dict['EMDDescription'] = self.emd_description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amount
        if self.amount:
            _dict['Amount'] = self.amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EMDSegment:
        """Create an instance of EMDSegment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EMDSegment.parse_obj(obj)

        _obj = EMDSegment.parse_obj({
            "type": obj.get("@type"),
            "sequence": obj.get("sequence"),
            "quantity": obj.get("quantity"),
            "emd_description": EMDDescription.from_dict(obj.get("EMDDescription")) if obj.get("EMDDescription") is not None else None,
            "amount": Amount.from_dict(obj.get("Amount")) if obj.get("Amount") is not None else None,
            "status": obj.get("Status"),
            "date_of_service": obj.get("DateOfService"),
            "present_to": obj.get("PresentTo"),
            "present_at": obj.get("PresentAt"),
            "routing": obj.get("Routing")
        })
        return _obj


