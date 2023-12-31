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
from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.three_domain_security_gateway import ThreeDomainSecurityGateway
from openapi_client.models.three_domain_security_results import ThreeDomainSecurityResults

class ThreeDomainSecurity(BaseModel):
    """
    ThreeDomainSecurity
    """
    type: Optional[StrictStr] = Field(None, alias="@type")
    three_domain_security_gateway: ThreeDomainSecurityGateway = Field(..., alias="ThreeDomainSecurityGateway")
    three_domain_security_results: ThreeDomainSecurityResults = Field(..., alias="ThreeDomainSecurityResults")
    __properties = ["@type", "ThreeDomainSecurityGateway", "ThreeDomainSecurityResults"]

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
    def from_json(cls, json_str: str) -> ThreeDomainSecurity:
        """Create an instance of ThreeDomainSecurity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of three_domain_security_gateway
        if self.three_domain_security_gateway:
            _dict['ThreeDomainSecurityGateway'] = self.three_domain_security_gateway.to_dict()
        # override the default output from pydantic by calling `to_dict()` of three_domain_security_results
        if self.three_domain_security_results:
            _dict['ThreeDomainSecurityResults'] = self.three_domain_security_results.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ThreeDomainSecurity:
        """Create an instance of ThreeDomainSecurity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ThreeDomainSecurity.parse_obj(obj)

        _obj = ThreeDomainSecurity.parse_obj({
            "type": obj.get("@type"),
            "three_domain_security_gateway": ThreeDomainSecurityGateway.from_dict(obj.get("ThreeDomainSecurityGateway")) if obj.get("ThreeDomainSecurityGateway") is not None else None,
            "three_domain_security_results": ThreeDomainSecurityResults.from_dict(obj.get("ThreeDomainSecurityResults")) if obj.get("ThreeDomainSecurityResults") is not None else None
        })
        return _obj


