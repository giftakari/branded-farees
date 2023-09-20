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

class PaymentAfterReservation(BaseModel):
    """
    PaymentAfterReservation
    """
    type: StrictStr = Field(..., alias="@type")
    time_of_day: Optional[StrictStr] = Field(None, alias="TimeOfDay", description="The time of day indicates the earliest time the Offer can be reserved. Used in conjunction with DayOfWeek or Duration")
    __properties = ["@type", "TimeOfDay"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    # JSON field name that stores the object type
    __discriminator_property_name = '@type'

    # discriminator mappings
    __discriminator_value_class_map = {
        'PaymentAfterReservationDayOfWeek': 'PaymentAfterReservationDayOfWeek',
        'PaymentAfterReservationDuration': 'PaymentAfterReservationDuration'
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
    def from_json(cls, json_str: str) -> Union(PaymentAfterReservationDayOfWeek, PaymentAfterReservationDuration):
        """Create an instance of PaymentAfterReservation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Union(PaymentAfterReservationDayOfWeek, PaymentAfterReservationDuration):
        """Create an instance of PaymentAfterReservation from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("PaymentAfterReservation failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

from openapi_client.models.payment_after_reservation_day_of_week import PaymentAfterReservationDayOfWeek
from openapi_client.models.payment_after_reservation_duration import PaymentAfterReservationDuration
PaymentAfterReservation.update_forward_refs()
