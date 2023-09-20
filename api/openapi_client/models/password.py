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
from pydantic import BaseModel, Field, StrictStr, constr, validator
from openapi_client.models.encryption_token_type_auth_enum import EncryptionTokenTypeAuthEnum
from openapi_client.models.error_warning import ErrorWarning

class Password(BaseModel):
    """
    Password
    """
    type: Optional[StrictStr] = Field(None, alias="@type")
    encryption_key: Optional[StrictStr] = Field(None, alias="encryptionKey", description="Note: This contains a key required to retrieve the full payment instrument details compliant with PCI DSS standards.")
    encryption_key_method: Optional[StrictStr] = Field(None, alias="encryptionKeyMethod", description="Developer: This contains a reference to the key generation method being used - this is NOT the key value.")
    encryption_method: Optional[StrictStr] = Field(None, alias="encryptionMethod", description="OpenTravel Best Practice: Encryption Method: When using the OpenTravel Encryption element, it is RECOMMENDED that all trading partners be informed of all encryption methods being used in advance of implementation to ensure message processing compatibility.")
    encrypted_value: Optional[StrictStr] = Field(None, alias="encryptedValue", description="Encrypted value")
    mask: Optional[constr(strict=True)] = Field(None, description="Masked Value")
    token: Optional[constr(strict=True)] = Field(None, description="Token value")
    token_provider_id: Optional[StrictStr] = Field(None, alias="tokenProviderID", description="Developer: This contains a provider ID if multiple providers are used for secure information exchange.")
    authentication_method: Optional[EncryptionTokenTypeAuthEnum] = Field(None, alias="authenticationMethod")
    plain_text: Optional[StrictStr] = Field(None, alias="PlainText", description="Don't use this unless it is REALLY ok to not use encryption. Non-secure (plain text) value.")
    error_warning: Optional[ErrorWarning] = Field(None, alias="ErrorWarning")
    __properties = ["@type", "encryptionKey", "encryptionKeyMethod", "encryptionMethod", "encryptedValue", "mask", "token", "tokenProviderID", "authenticationMethod", "PlainText", "ErrorWarning"]

    @validator('mask')
    def mask_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[0-9a-zA-Z]{1,32}", value):
            raise ValueError(r"must validate the regular expression /[0-9a-zA-Z]{1,32}/")
        return value

    @validator('token')
    def token_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[0-9a-zA-Z]{1,32}", value):
            raise ValueError(r"must validate the regular expression /[0-9a-zA-Z]{1,32}/")
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
    def from_json(cls, json_str: str) -> Password:
        """Create an instance of Password from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of error_warning
        if self.error_warning:
            _dict['ErrorWarning'] = self.error_warning.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Password:
        """Create an instance of Password from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Password.parse_obj(obj)

        _obj = Password.parse_obj({
            "type": obj.get("@type"),
            "encryption_key": obj.get("encryptionKey"),
            "encryption_key_method": obj.get("encryptionKeyMethod"),
            "encryption_method": obj.get("encryptionMethod"),
            "encrypted_value": obj.get("encryptedValue"),
            "mask": obj.get("mask"),
            "token": obj.get("token"),
            "token_provider_id": obj.get("tokenProviderID"),
            "authentication_method": obj.get("authenticationMethod"),
            "plain_text": obj.get("PlainText"),
            "error_warning": ErrorWarning.from_dict(obj.get("ErrorWarning")) if obj.get("ErrorWarning") is not None else None
        })
        return _obj


