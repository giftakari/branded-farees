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
from openapi_client.models.form_of_payment_response import FormOfPaymentResponse

class FormOfPaymentResponseWrapper(BaseModel):
    """
    FormOfPaymentResponseWrapper
    """
    form_of_payment_response: Optional[FormOfPaymentResponse] = Field(None, alias="FormOfPaymentResponse")
    __properties = ["FormOfPaymentResponse"]

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
    def from_json(cls, json_str: str) -> FormOfPaymentResponseWrapper:
        """Create an instance of FormOfPaymentResponseWrapper from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of form_of_payment_response
        if self.form_of_payment_response:
            _dict['FormOfPaymentResponse'] = self.form_of_payment_response.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FormOfPaymentResponseWrapper:
        """Create an instance of FormOfPaymentResponseWrapper from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FormOfPaymentResponseWrapper.parse_obj(obj)

        _obj = FormOfPaymentResponseWrapper.parse_obj({
            "form_of_payment_response": FormOfPaymentResponse.from_dict(obj.get("FormOfPaymentResponse")) if obj.get("FormOfPaymentResponse") is not None else None
        })
        return _obj


