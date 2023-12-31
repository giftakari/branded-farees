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
from openapi_client.models.text_title_and_description import TextTitleAndDescription

class CheckInOutPolicy(BaseModel):
    """
    CheckInOutPolicy
    """
    type: Optional[StrictStr] = Field(None, alias="@type")
    check_in_time: constr(strict=True) = Field(..., alias="checkInTime", description="Check-in time")
    check_out_time: constr(strict=True) = Field(..., alias="checkOutTime", description="Check-out time")
    minimum_age: Optional[StrictInt] = Field(None, alias="minimumAge", description="Minimum age of guest checking in or out")
    description: Optional[conlist(TextTitleAndDescription, max_items=10)] = Field(None, alias="Description")
    __properties = ["@type", "checkInTime", "checkOutTime", "minimumAge", "Description"]

    @validator('check_in_time')
    def check_in_time_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"(([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)((:?)[0-5]\d)?([\.,]\d+(?!:))?", value):
            raise ValueError(r"must validate the regular expression /(([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)((:?)[0-5]\d)?([\.,]\d+(?!:))?/")
        return value

    @validator('check_out_time')
    def check_out_time_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"(([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)((:?)[0-5]\d)?([\.,]\d+(?!:))?", value):
            raise ValueError(r"must validate the regular expression /(([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)((:?)[0-5]\d)?([\.,]\d+(?!:))?/")
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
    def from_json(cls, json_str: str) -> CheckInOutPolicy:
        """Create an instance of CheckInOutPolicy from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in description (list)
        _items = []
        if self.description:
            for _item in self.description:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Description'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CheckInOutPolicy:
        """Create an instance of CheckInOutPolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CheckInOutPolicy.parse_obj(obj)

        _obj = CheckInOutPolicy.parse_obj({
            "type": obj.get("@type"),
            "check_in_time": obj.get("checkInTime"),
            "check_out_time": obj.get("checkOutTime"),
            "minimum_age": obj.get("minimumAge"),
            "description": [TextTitleAndDescription.from_dict(_item) for _item in obj.get("Description")] if obj.get("Description") is not None else None
        })
        return _obj


