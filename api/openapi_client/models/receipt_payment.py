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
from pydantic import Field, conlist
from openapi_client.models.document import Document
from openapi_client.models.identifier import Identifier
from openapi_client.models.payment_identifier import PaymentIdentifier
from openapi_client.models.receipt import Receipt

class ReceiptPayment(Receipt):
    """
    ReceiptPayment
    """
    payment_identifier: Optional[PaymentIdentifier] = Field(None, alias="PaymentIdentifier")
    document: Optional[conlist(Document, max_items=100)] = Field(None, alias="Document")
    __properties = ["@type", "id", "ReceiptRef", "Identifier", "dateTime", "OfferRef", "ProductRef", "PaymentIdentifier", "Document"]

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
    def from_json(cls, json_str: str) -> ReceiptPayment:
        """Create an instance of ReceiptPayment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of identifier
        if self.identifier:
            _dict['Identifier'] = self.identifier.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_identifier
        if self.payment_identifier:
            _dict['PaymentIdentifier'] = self.payment_identifier.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in document (list)
        _items = []
        if self.document:
            for _item in self.document:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Document'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReceiptPayment:
        """Create an instance of ReceiptPayment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReceiptPayment.parse_obj(obj)

        _obj = ReceiptPayment.parse_obj({
            "type": obj.get("@type"),
            "id": obj.get("id"),
            "receipt_ref": obj.get("ReceiptRef"),
            "identifier": Identifier.from_dict(obj.get("Identifier")) if obj.get("Identifier") is not None else None,
            "date_time": obj.get("dateTime"),
            "offer_ref": obj.get("OfferRef"),
            "product_ref": obj.get("ProductRef"),
            "payment_identifier": PaymentIdentifier.from_dict(obj.get("PaymentIdentifier")) if obj.get("PaymentIdentifier") is not None else None,
            "document": [Document.from_dict(_item) for _item in obj.get("Document")] if obj.get("Document") is not None else None
        })
        return _obj


