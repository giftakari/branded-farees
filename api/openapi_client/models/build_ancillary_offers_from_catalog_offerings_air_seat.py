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
from openapi_client.models.build_ancillary_offers_from_catalog_offerings import BuildAncillaryOffersFromCatalogOfferings
from openapi_client.models.offer_query_build_ancillary_offers_from_catalog_offerings import OfferQueryBuildAncillaryOffersFromCatalogOfferings

class BuildAncillaryOffersFromCatalogOfferingsAirSeat(OfferQueryBuildAncillaryOffersFromCatalogOfferings):
    """
    BuildAncillaryOffersFromCatalogOfferingsAirSeat
    """
    seat_assignment: constr(strict=True, max_length=32) = Field(..., alias="SeatAssignment", description="The specific seat number to be assigned to a Traveler")
    __properties = ["@type", "BuildAncillaryOffersFromCatalogOfferings", "SeatAssignment"]

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
    def from_json(cls, json_str: str) -> BuildAncillaryOffersFromCatalogOfferingsAirSeat:
        """Create an instance of BuildAncillaryOffersFromCatalogOfferingsAirSeat from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in build_ancillary_offers_from_catalog_offerings (list)
        _items = []
        if self.build_ancillary_offers_from_catalog_offerings:
            for _item in self.build_ancillary_offers_from_catalog_offerings:
                if _item:
                    _items.append(_item.to_dict())
            _dict['BuildAncillaryOffersFromCatalogOfferings'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BuildAncillaryOffersFromCatalogOfferingsAirSeat:
        """Create an instance of BuildAncillaryOffersFromCatalogOfferingsAirSeat from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BuildAncillaryOffersFromCatalogOfferingsAirSeat.parse_obj(obj)

        _obj = BuildAncillaryOffersFromCatalogOfferingsAirSeat.parse_obj({
            "type": obj.get("@type"),
            "build_ancillary_offers_from_catalog_offerings": [BuildAncillaryOffersFromCatalogOfferings.from_dict(_item) for _item in obj.get("BuildAncillaryOffersFromCatalogOfferings")] if obj.get("BuildAncillaryOffersFromCatalogOfferings") is not None else None,
            "seat_assignment": obj.get("SeatAssignment")
        })
        return _obj


