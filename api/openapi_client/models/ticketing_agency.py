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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist, constr, validator

class TicketingAgency(BaseModel):
    """
    TicketingAgency
    """
    type: Optional[StrictStr] = Field(None, alias="@type")
    code: constr(strict=True, max_length=10, min_length=2) = Field(..., alias="Code", description="The code of the ticketing agency")
    product_ref: Optional[conlist(StrictStr)] = Field(None, alias="ProductRef", description="The Product Ref the TicketingAgency applies to")
    segment_sequence_list: Optional[conlist(StrictInt)] = Field(None, alias="SegmentSequenceList", description="The segmentSequenceList the TicketingAgency applies to")
    __properties = ["@type", "Code", "ProductRef", "SegmentSequenceList"]

    @validator('code')
    def code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
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
    def from_json(cls, json_str: str) -> TicketingAgency:
        """Create an instance of TicketingAgency from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TicketingAgency:
        """Create an instance of TicketingAgency from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TicketingAgency.parse_obj(obj)

        _obj = TicketingAgency.parse_obj({
            "type": obj.get("@type"),
            "code": obj.get("Code"),
            "product_ref": obj.get("ProductRef"),
            "segment_sequence_list": obj.get("SegmentSequenceList")
        })
        return _obj


