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
from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.identifier import Identifier

class FlightID(BaseModel):
    """
    FlightID
    """
    type: StrictStr = Field(..., alias="@type")
    id: Optional[StrictStr] = Field(None, description="Internal ID")
    flight_ref: Optional[StrictStr] = Field(None, alias="FlightRef", description="Reference to a Flight object eslewhere in the message")
    identifier: Optional[Identifier] = Field(None, alias="Identifier")
    __properties = ["@type", "id", "FlightRef", "Identifier"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    # JSON field name that stores the object type
    __discriminator_property_name = '@type'

    # discriminator mappings
    __discriminator_value_class_map = {
        'Flight': 'Flight',
        'FlightDetail': 'FlightDetail',
        'ImportsCatalogAir_ReservationResource': 'ImportsCatalogAirReservationResource'
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
    def from_json(cls, json_str: str) -> Union(Flight, FlightDetail, ImportsCatalogAirReservationResource):
        """Create an instance of FlightID from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Union(Flight, FlightDetail, ImportsCatalogAirReservationResource):
        """Create an instance of FlightID from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("FlightID failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

from openapi_client.models.flight import Flight
from openapi_client.models.flight_detail import FlightDetail
from openapi_client.models.imports_catalog_air_reservation_resource import ImportsCatalogAir_ReservationResource
FlightID.update_forward_refs()

