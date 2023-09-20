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
from pydantic import BaseModel, Field
from openapi_client.models.reservation_comment_list_response import ReservationCommentListResponse

class ReservationCommentListResponseWrapper(BaseModel):
    """
    ReservationCommentListResponseWrapper
    """
    reservation_comment_list_response: Optional[ReservationCommentListResponse] = Field(None, alias="ReservationCommentListResponse")
    __properties = ["ReservationCommentListResponse"]

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
    def from_json(cls, json_str: str) -> ReservationCommentListResponseWrapper:
        """Create an instance of ReservationCommentListResponseWrapper from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of reservation_comment_list_response
        if self.reservation_comment_list_response:
            _dict['ReservationCommentListResponse'] = self.reservation_comment_list_response.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReservationCommentListResponseWrapper:
        """Create an instance of ReservationCommentListResponseWrapper from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReservationCommentListResponseWrapper.parse_obj(obj)

        _obj = ReservationCommentListResponseWrapper.parse_obj({
            "reservation_comment_list_response": ReservationCommentListResponse.from_dict(obj.get("ReservationCommentListResponse")) if obj.get("ReservationCommentListResponse") is not None else None
        })
        return _obj


