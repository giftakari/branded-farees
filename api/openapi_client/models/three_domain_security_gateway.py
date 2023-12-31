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
from pydantic import BaseModel, Field, StrictStr, constr
from openapi_client.models.authentication_verification import AuthenticationVerification
from openapi_client.models.password import Password

class ThreeDomainSecurityGateway(BaseModel):
    """
    ThreeDomainSecurityGateway
    """
    type: Optional[StrictStr] = Field(None, alias="@type")
    e_ci: Optional[constr(strict=True, max_length=1)] = Field(None, alias="eCI", description="The eCI value")
    merchant_id: Optional[StrictStr] = Field(None, alias="merchantID", description="The merchant ID value")
    processor_id: Optional[StrictStr] = Field(None, alias="processorID", description="The processor ID value")
    u_rl: Optional[StrictStr] = Field(None, alias="uRL", description="Transaction URL.")
    authentication_verification: Optional[AuthenticationVerification] = Field(None, alias="AuthenticationVerification")
    password: Optional[Password] = Field(None, alias="Password")
    __properties = ["@type", "eCI", "merchantID", "processorID", "uRL", "AuthenticationVerification", "Password"]

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
    def from_json(cls, json_str: str) -> ThreeDomainSecurityGateway:
        """Create an instance of ThreeDomainSecurityGateway from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of authentication_verification
        if self.authentication_verification:
            _dict['AuthenticationVerification'] = self.authentication_verification.to_dict()
        # override the default output from pydantic by calling `to_dict()` of password
        if self.password:
            _dict['Password'] = self.password.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ThreeDomainSecurityGateway:
        """Create an instance of ThreeDomainSecurityGateway from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ThreeDomainSecurityGateway.parse_obj(obj)

        _obj = ThreeDomainSecurityGateway.parse_obj({
            "type": obj.get("@type"),
            "e_ci": obj.get("eCI"),
            "merchant_id": obj.get("merchantID"),
            "processor_id": obj.get("processorID"),
            "u_rl": obj.get("uRL"),
            "authentication_verification": AuthenticationVerification.from_dict(obj.get("AuthenticationVerification")) if obj.get("AuthenticationVerification") is not None else None,
            "password": Password.from_dict(obj.get("Password")) if obj.get("Password") is not None else None
        })
        return _obj


