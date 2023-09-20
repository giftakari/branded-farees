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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictStr, conlist
from openapi_client.models.accounting_id import AccountingID
from openapi_client.models.document_overrides_id import DocumentOverridesID
from openapi_client.models.form_of_payment_id import FormOfPaymentID
from openapi_client.models.payment_id import PaymentID
from openapi_client.models.preference_id import PreferenceID
from openapi_client.models.primary_contact_id import PrimaryContactID
from openapi_client.models.receipt_confirmation import ReceiptConfirmation
from openapi_client.models.reservation_comment_id import ReservationCommentID
from openapi_client.models.special_service_id import SpecialServiceID
from openapi_client.models.travel_agency import TravelAgency
from openapi_client.models.traveler_id import TravelerID

class ReservationBuild(BaseModel):
    """
    ReservationBuild
    """
    type: StrictStr = Field(..., alias="@type")
    traveler: conlist(TravelerID, max_items=9, min_items=1) = Field(..., alias="Traveler")
    form_of_payment: Optional[conlist(FormOfPaymentID, max_items=100)] = Field(None, alias="FormOfPayment")
    payment: Optional[conlist(PaymentID, max_items=100)] = Field(None, alias="Payment")
    reservation_comment: Optional[conlist(ReservationCommentID, max_items=1000)] = Field(None, alias="ReservationComment")
    primary_contact: Optional[conlist(PrimaryContactID, max_items=10)] = Field(None, alias="PrimaryContact")
    special_service: Optional[conlist(SpecialServiceID, max_items=100)] = Field(None, alias="SpecialService")
    accounting: Optional[AccountingID] = Field(None, alias="Accounting")
    document_overrides: Optional[conlist(DocumentOverridesID, max_items=5)] = Field(None, alias="DocumentOverrides")
    preference: Optional[conlist(PreferenceID, max_items=100)] = Field(None, alias="Preference")
    receipt_confirmation: Optional[ReceiptConfirmation] = Field(None, alias="ReceiptConfirmation")
    travel_agency: Optional[TravelAgency] = Field(None, alias="TravelAgency")
    __properties = ["@type", "Traveler", "FormOfPayment", "Payment", "ReservationComment", "PrimaryContact", "SpecialService", "Accounting", "DocumentOverrides", "Preference", "ReceiptConfirmation", "TravelAgency"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    # JSON field name that stores the object type
    __discriminator_property_name = '@type'

    # discriminator mappings
    __discriminator_value_class_map = {
        'ReservationBuildFromCatalogOffering': 'ReservationBuildFromCatalogOffering',
        'ReservationBuildFromCatalogOfferings': 'ReservationBuildFromCatalogOfferings',
        'ReservationBuildFromCatalogOfferingsAir': 'ReservationBuildFromCatalogOfferingsAir',
        'ReservationBuildFromCatalogProductOfferings': 'ReservationBuildFromCatalogProductOfferings',
        'ReservationBuildFromProducts': 'ReservationBuildFromProducts',
        'ReservationBuildVehicle': 'ReservationBuildVehicle'
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
    def from_json(cls, json_str: str) -> Union(ReservationBuildFromCatalogOffering, ReservationBuildFromCatalogOfferings, ReservationBuildFromCatalogOfferingsAir, ReservationBuildFromCatalogProductOfferings, ReservationBuildFromProducts, ReservationBuildVehicle):
        """Create an instance of ReservationBuild from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in traveler (list)
        _items = []
        if self.traveler:
            for _item in self.traveler:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Traveler'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in form_of_payment (list)
        _items = []
        if self.form_of_payment:
            for _item in self.form_of_payment:
                if _item:
                    _items.append(_item.to_dict())
            _dict['FormOfPayment'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in payment (list)
        _items = []
        if self.payment:
            for _item in self.payment:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Payment'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in reservation_comment (list)
        _items = []
        if self.reservation_comment:
            for _item in self.reservation_comment:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ReservationComment'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in primary_contact (list)
        _items = []
        if self.primary_contact:
            for _item in self.primary_contact:
                if _item:
                    _items.append(_item.to_dict())
            _dict['PrimaryContact'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in special_service (list)
        _items = []
        if self.special_service:
            for _item in self.special_service:
                if _item:
                    _items.append(_item.to_dict())
            _dict['SpecialService'] = _items
        # override the default output from pydantic by calling `to_dict()` of accounting
        if self.accounting:
            _dict['Accounting'] = self.accounting.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in document_overrides (list)
        _items = []
        if self.document_overrides:
            for _item in self.document_overrides:
                if _item:
                    _items.append(_item.to_dict())
            _dict['DocumentOverrides'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in preference (list)
        _items = []
        if self.preference:
            for _item in self.preference:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Preference'] = _items
        # override the default output from pydantic by calling `to_dict()` of receipt_confirmation
        if self.receipt_confirmation:
            _dict['ReceiptConfirmation'] = self.receipt_confirmation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of travel_agency
        if self.travel_agency:
            _dict['TravelAgency'] = self.travel_agency.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Union(ReservationBuildFromCatalogOffering, ReservationBuildFromCatalogOfferings, ReservationBuildFromCatalogOfferingsAir, ReservationBuildFromCatalogProductOfferings, ReservationBuildFromProducts, ReservationBuildVehicle):
        """Create an instance of ReservationBuild from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("ReservationBuild failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

from openapi_client.models.reservation_build_from_catalog_offering import ReservationBuildFromCatalogOffering
from openapi_client.models.reservation_build_from_catalog_offerings import ReservationBuildFromCatalogOfferings
from openapi_client.models.reservation_build_from_catalog_offerings_air import ReservationBuildFromCatalogOfferingsAir
from openapi_client.models.reservation_build_from_catalog_product_offerings import ReservationBuildFromCatalogProductOfferings
from openapi_client.models.reservation_build_from_products import ReservationBuildFromProducts
from openapi_client.models.reservation_build_vehicle import ReservationBuildVehicle
ReservationBuild.update_forward_refs()
