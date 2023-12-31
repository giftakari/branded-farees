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


from typing import Optional, Union
from pydantic import Field, StrictInt, StrictStr
from openapi_client.models.amount import Amount
from openapi_client.models.ancillary_description import AncillaryDescription
from openapi_client.models.commission import Commission
from openapi_client.models.discount import Discount
from openapi_client.models.price_breakdown import PriceBreakdown
from openapi_client.models.traveler_identifier_ref import TravelerIdentifierRef

class PriceBreakdownAncillary(PriceBreakdown):
    """
    PriceBreakdownAncillary
    """
    quantity: Optional[StrictInt] = Field(None, description="The quantity of ancillary items included in this PriceBreakdown")
    description: Optional[AncillaryDescription] = Field(None, alias="Description")
    product_ref: Optional[StrictStr] = Field(None, alias="ProductRef", description="The product ref this PriceBreakdown applies to. If no productRef exists then the PriceBreakdown applies to all Products within the Offer.")
    discount: Optional[Discount] = Field(None, alias="Discount")
    traveler_identifier_ref: Optional[TravelerIdentifierRef] = Field(None, alias="TravelerIdentifierRef")
    __properties = ["@type", "Amount", "Commission", "quantity", "Description", "ProductRef", "Discount", "TravelerIdentifierRef"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    # JSON field name that stores the object type
    __discriminator_property_name = '@type'

    # discriminator mappings
    __discriminator_value_class_map = {
        'PriceBreakdownAncillaryAir': 'PriceBreakdownAncillaryAir',
        'PriceBreakdownAncillaryVehicle': 'PriceBreakdownAncillaryVehicle'
    }

    @classmethod
    def get_discriminator_value(cls, obj: dict) -> str:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Union(PriceBreakdownAncillaryAir, PriceBreakdownAncillaryVehicle):
        """Create an instance of PriceBreakdownAncillary from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of amount
        if self.amount:
            _dict['Amount'] = self.amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of commission
        if self.commission:
            _dict['Commission'] = self.commission.to_dict()
        # override the default output from pydantic by calling `to_dict()` of description
        if self.description:
            _dict['Description'] = self.description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of discount
        if self.discount:
            _dict['Discount'] = self.discount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of traveler_identifier_ref
        if self.traveler_identifier_ref:
            _dict['TravelerIdentifierRef'] = self.traveler_identifier_ref.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Union(PriceBreakdownAncillaryAir, PriceBreakdownAncillaryVehicle):
        """Create an instance of PriceBreakdownAncillary from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("PriceBreakdownAncillary failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

from openapi_client.models.price_breakdown_ancillary_air import PriceBreakdownAncillaryAir
from openapi_client.models.price_breakdown_ancillary_vehicle import PriceBreakdownAncillaryVehicle
PriceBreakdownAncillary.update_forward_refs()

