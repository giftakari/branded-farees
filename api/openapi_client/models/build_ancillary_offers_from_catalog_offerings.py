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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conint
from openapi_client.models.catalog_offering_identifier import CatalogOfferingIdentifier
from openapi_client.models.catalog_offerings_identifier import CatalogOfferingsIdentifier
from openapi_client.models.identifier import Identifier
from openapi_client.models.product_identifier import ProductIdentifier
from openapi_client.models.traveler_identifier_ref import TravelerIdentifierRef

class BuildAncillaryOffersFromCatalogOfferings(BaseModel):
    """
    BuildAncillaryOffersFromCatalogOfferings
    """
    type: StrictStr = Field(..., alias="@type")
    catalog_offerings_identifier: CatalogOfferingsIdentifier = Field(..., alias="CatalogOfferingsIdentifier")
    catalog_offering_identifier: CatalogOfferingIdentifier = Field(..., alias="CatalogOfferingIdentifier")
    product_identifier: ProductIdentifier = Field(..., alias="ProductIdentifier")
    quantity: Optional[conint(strict=True, ge=0)] = Field(None, alias="Quantity", description="The quantity of ancillaries to be included in the Offer")
    traveler_identifier_ref: Optional[TravelerIdentifierRef] = Field(None, alias="TravelerIdentifierRef")
    catalog_offerings_ancillary_list_identifier: Optional[Identifier] = Field(None, alias="CatalogOfferingsAncillaryListIdentifier")
    include_unsellable_ancillaries_ind: Optional[StrictBool] = Field(None, alias="includeUnsellableAncillariesInd", description="If true, the response will include unsellable ancillary options")
    __properties = ["@type", "CatalogOfferingsIdentifier", "CatalogOfferingIdentifier", "ProductIdentifier", "Quantity", "TravelerIdentifierRef", "CatalogOfferingsAncillaryListIdentifier", "includeUnsellableAncillariesInd"]

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
    def from_json(cls, json_str: str) -> BuildAncillaryOffersFromCatalogOfferings:
        """Create an instance of BuildAncillaryOffersFromCatalogOfferings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of catalog_offerings_identifier
        if self.catalog_offerings_identifier:
            _dict['CatalogOfferingsIdentifier'] = self.catalog_offerings_identifier.to_dict()
        # override the default output from pydantic by calling `to_dict()` of catalog_offering_identifier
        if self.catalog_offering_identifier:
            _dict['CatalogOfferingIdentifier'] = self.catalog_offering_identifier.to_dict()
        # override the default output from pydantic by calling `to_dict()` of product_identifier
        if self.product_identifier:
            _dict['ProductIdentifier'] = self.product_identifier.to_dict()
        # override the default output from pydantic by calling `to_dict()` of traveler_identifier_ref
        if self.traveler_identifier_ref:
            _dict['TravelerIdentifierRef'] = self.traveler_identifier_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of catalog_offerings_ancillary_list_identifier
        if self.catalog_offerings_ancillary_list_identifier:
            _dict['CatalogOfferingsAncillaryListIdentifier'] = self.catalog_offerings_ancillary_list_identifier.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BuildAncillaryOffersFromCatalogOfferings:
        """Create an instance of BuildAncillaryOffersFromCatalogOfferings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BuildAncillaryOffersFromCatalogOfferings.parse_obj(obj)

        _obj = BuildAncillaryOffersFromCatalogOfferings.parse_obj({
            "type": obj.get("@type"),
            "catalog_offerings_identifier": CatalogOfferingsIdentifier.from_dict(obj.get("CatalogOfferingsIdentifier")) if obj.get("CatalogOfferingsIdentifier") is not None else None,
            "catalog_offering_identifier": CatalogOfferingIdentifier.from_dict(obj.get("CatalogOfferingIdentifier")) if obj.get("CatalogOfferingIdentifier") is not None else None,
            "product_identifier": ProductIdentifier.from_dict(obj.get("ProductIdentifier")) if obj.get("ProductIdentifier") is not None else None,
            "quantity": obj.get("Quantity"),
            "traveler_identifier_ref": TravelerIdentifierRef.from_dict(obj.get("TravelerIdentifierRef")) if obj.get("TravelerIdentifierRef") is not None else None,
            "catalog_offerings_ancillary_list_identifier": Identifier.from_dict(obj.get("CatalogOfferingsAncillaryListIdentifier")) if obj.get("CatalogOfferingsAncillaryListIdentifier") is not None else None,
            "include_unsellable_ancillaries_ind": obj.get("includeUnsellableAncillariesInd")
        })
        return _obj


