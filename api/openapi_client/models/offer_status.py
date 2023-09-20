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


from typing import Union
from pydantic import BaseModel, Field, StrictStr

class OfferStatus(BaseModel):
    """
    OfferStatus
    """
    type: StrictStr = Field(..., alias="@type")
    __properties = ["@type"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    # JSON field name that stores the object type
    __discriminator_property_name = '@type'

    # discriminator mappings
    __discriminator_value_class_map = {
        'OfferStatusAir': 'OfferStatusAir',
        'OfferStatusAncillary': 'OfferStatusAncillary',
        'OfferStatusHospitality': 'OfferStatusHospitality',
        'OfferStatusVehicle': 'OfferStatusVehicle'
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
    def from_json(cls, json_str: str) -> Union(OfferStatusAir, OfferStatusAncillary, OfferStatusHospitality, OfferStatusVehicle):
        """Create an instance of OfferStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Union(OfferStatusAir, OfferStatusAncillary, OfferStatusHospitality, OfferStatusVehicle):
        """Create an instance of OfferStatus from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("OfferStatus failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

from openapi_client.models.offer_status_air import OfferStatusAir
from openapi_client.models.offer_status_ancillary import OfferStatusAncillary
from openapi_client.models.offer_status_hospitality import OfferStatusHospitality
from openapi_client.models.offer_status_vehicle import OfferStatusVehicle
OfferStatus.update_forward_refs()

