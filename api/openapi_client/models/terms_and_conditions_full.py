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

from datetime import datetime
from typing import List, Optional, Union
from pydantic import Field, conlist
from openapi_client.models.customer_loyalty import CustomerLoyalty
from openapi_client.models.identifier import Identifier
from openapi_client.models.terms_and_conditions_full_id import TermsAndConditionsFullID
from openapi_client.models.text_block import TextBlock

class TermsAndConditionsFull(TermsAndConditionsFullID):
    """
    TermsAndConditionsFull
    """
    expiry_date: Optional[datetime] = Field(None, alias="ExpiryDate", description="The data and time the offer will expire")
    customer_loyalty: Optional[conlist(CustomerLoyalty, max_items=5)] = Field(None, alias="CustomerLoyalty")
    text_block: Optional[conlist(TextBlock, max_items=50)] = Field(None, alias="TextBlock")
    __properties = ["@type", "id", "termsAndConditionsRef", "Identifier", "ExpiryDate", "CustomerLoyalty", "TextBlock"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    # JSON field name that stores the object type
    __discriminator_property_name = '@type'

    # discriminator mappings
    __discriminator_value_class_map = {
        'ImportsCatalogAir_ReservationResource': 'ImportsCatalogAirReservationResource',
        'TermsAndConditionsFullAir': 'TermsAndConditionsFullAir',
        'TermsAndConditionsFullAirChange': 'TermsAndConditionsFullAirChange',
        'TermsAndConditionsFullAncillary': 'TermsAndConditionsFullAncillary',
        'TermsAndConditionsFullHospitality': 'TermsAndConditionsFullHospitality',
        'TermsAndConditionsFullVehicle': 'TermsAndConditionsFullVehicle'
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
    def from_json(cls, json_str: str) -> Union(TermsAndConditionsFullAir, TermsAndConditionsFullAirChange, TermsAndConditionsFullAncillary, TermsAndConditionsFullHospitality, TermsAndConditionsFullVehicle):
        """Create an instance of TermsAndConditionsFull from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in customer_loyalty (list)
        _items = []
        if self.customer_loyalty:
            for _item in self.customer_loyalty:
                if _item:
                    _items.append(_item.to_dict())
            _dict['CustomerLoyalty'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in text_block (list)
        _items = []
        if self.text_block:
            for _item in self.text_block:
                if _item:
                    _items.append(_item.to_dict())
            _dict['TextBlock'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Union(TermsAndConditionsFullAir, TermsAndConditionsFullAirChange, TermsAndConditionsFullAncillary, TermsAndConditionsFullHospitality, TermsAndConditionsFullVehicle):
        """Create an instance of TermsAndConditionsFull from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("TermsAndConditionsFull failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

from openapi_client.models.imports_catalog_air_reservation_resource import ImportsCatalogAir_ReservationResource
from openapi_client.models.terms_and_conditions_full_air import TermsAndConditionsFullAir
from openapi_client.models.terms_and_conditions_full_air_change import TermsAndConditionsFullAirChange
from openapi_client.models.terms_and_conditions_full_ancillary import TermsAndConditionsFullAncillary
from openapi_client.models.terms_and_conditions_full_hospitality import TermsAndConditionsFullHospitality
from openapi_client.models.terms_and_conditions_full_vehicle import TermsAndConditionsFullVehicle
TermsAndConditionsFull.update_forward_refs()

