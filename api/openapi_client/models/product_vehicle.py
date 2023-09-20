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
from pydantic import Field
from openapi_client.models.identifier import Identifier
from openapi_client.models.product import Product
from openapi_client.models.vehicle import Vehicle

class ProductVehicle(Product):
    """
    ProductVehicle
    """
    vehicle: Optional[Vehicle] = Field(None, alias="Vehicle")
    __properties = ["@type", "id", "productRef", "Identifier", "Quantity", "Vehicle"]

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
    def from_json(cls, json_str: str) -> ProductVehicle:
        """Create an instance of ProductVehicle from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of vehicle
        if self.vehicle:
            _dict['Vehicle'] = self.vehicle.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProductVehicle:
        """Create an instance of ProductVehicle from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProductVehicle.parse_obj(obj)

        _obj = ProductVehicle.parse_obj({
            "type": obj.get("@type"),
            "id": obj.get("id"),
            "product_ref": obj.get("productRef"),
            "identifier": Identifier.from_dict(obj.get("Identifier")) if obj.get("Identifier") is not None else None,
            "quantity": obj.get("Quantity"),
            "vehicle": Vehicle.from_dict(obj.get("Vehicle")) if obj.get("Vehicle") is not None else None
        })
        return _obj

