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



from pydantic import Field, constr
from openapi_client.models.amount import Amount
from openapi_client.models.commission import Commission
from openapi_client.models.cumulative_value import CumulativeValue
from openapi_client.models.document import Document
from openapi_client.models.filed_amount import FiledAmount
from openapi_client.models.traveler_identifier_ref import TravelerIdentifierRef
from openapi_client.models.waiver_code import WaiverCode

class DocumentMCORefund(Document):
    """
    DocumentMCORefund
    """
    control_number: constr(strict=True, max_length=32) = Field(..., alias="ControlNumber", description="Reference for tracking refund")
    __properties = ["@type", "Number", "TravelerIdentifierRef", "Amount", "WaiverCode", "Commission", "CumulativeValue", "IssuingPCC", "IssuingIATA", "IssuingCity", "FiledAmount", "ControlNumber"]

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
    def from_json(cls, json_str: str) -> DocumentMCORefund:
        """Create an instance of DocumentMCORefund from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of traveler_identifier_ref
        if self.traveler_identifier_ref:
            _dict['TravelerIdentifierRef'] = self.traveler_identifier_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amount
        if self.amount:
            _dict['Amount'] = self.amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of waiver_code
        if self.waiver_code:
            _dict['WaiverCode'] = self.waiver_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of commission
        if self.commission:
            _dict['Commission'] = self.commission.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cumulative_value
        if self.cumulative_value:
            _dict['CumulativeValue'] = self.cumulative_value.to_dict()
        # override the default output from pydantic by calling `to_dict()` of filed_amount
        if self.filed_amount:
            _dict['FiledAmount'] = self.filed_amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DocumentMCORefund:
        """Create an instance of DocumentMCORefund from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DocumentMCORefund.parse_obj(obj)

        _obj = DocumentMCORefund.parse_obj({
            "type": obj.get("@type"),
            "number": obj.get("Number"),
            "traveler_identifier_ref": TravelerIdentifierRef.from_dict(obj.get("TravelerIdentifierRef")) if obj.get("TravelerIdentifierRef") is not None else None,
            "amount": Amount.from_dict(obj.get("Amount")) if obj.get("Amount") is not None else None,
            "waiver_code": WaiverCode.from_dict(obj.get("WaiverCode")) if obj.get("WaiverCode") is not None else None,
            "commission": Commission.from_dict(obj.get("Commission")) if obj.get("Commission") is not None else None,
            "cumulative_value": CumulativeValue.from_dict(obj.get("CumulativeValue")) if obj.get("CumulativeValue") is not None else None,
            "issuing_pcc": obj.get("IssuingPCC"),
            "issuing_iata": obj.get("IssuingIATA"),
            "issuing_city": obj.get("IssuingCity"),
            "filed_amount": FiledAmount.from_dict(obj.get("FiledAmount")) if obj.get("FiledAmount") is not None else None,
            "control_number": obj.get("ControlNumber")
        })
        return _obj


