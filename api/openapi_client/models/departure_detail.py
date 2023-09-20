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
from openapi_client.models.departure import Departure

class DepartureDetail(Departure):
    """
    DepartureDetail
    """
    terminal: Optional[constr(strict=True, max_length=4096)] = Field(None, description="Departure/Arrival terminal")
    country: Optional[constr(strict=True)] = Field(None, description="Country of to departure or arrival")
    __properties = ["@type", "location", "date", "time", "terminal", "country"]

    @validator('terminal')
    def terminal_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"([0-9a-zA-Z]+)?", value):
            raise ValueError(r"must validate the regular expression /([0-9a-zA-Z]+)?/")
        return value

    @validator('country')
    def country_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[a-zA-Z]{2}", value):
            raise ValueError(r"must validate the regular expression /[a-zA-Z]{2}/")
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
    def from_json(cls, json_str: str) -> DepartureDetail:
        """Create an instance of DepartureDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DepartureDetail:
        """Create an instance of DepartureDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DepartureDetail.parse_obj(obj)

        _obj = DepartureDetail.parse_obj({
            "type": obj.get("@type"),
            "location": obj.get("location"),
            "var_date": obj.get("date"),
            "time": obj.get("time"),
            "terminal": obj.get("terminal"),
            "country": obj.get("country")
        })
        return _obj

