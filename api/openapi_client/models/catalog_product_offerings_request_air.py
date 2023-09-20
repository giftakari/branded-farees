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
from pydantic import Field, StrictBool, conint, conlist
from openapi_client.models.catalog_product_offerings_request import CatalogProductOfferingsRequest
from openapi_client.models.content_source_enum import ContentSourceEnum
from openapi_client.models.custom_response_modifiers_air import CustomResponseModifiersAir
from openapi_client.models.passenger_criteria import PassengerCriteria
from openapi_client.models.payment_criteria import PaymentCriteria
from openapi_client.models.pricing_modifiers_air import PricingModifiersAir
from openapi_client.models.pseudo_city_info import PseudoCityInfo
from openapi_client.models.search_control_console_channel_id import SearchControlConsoleChannelID
from openapi_client.models.search_criteria_flight import SearchCriteriaFlight
from openapi_client.models.search_modifiers_air import SearchModifiersAir
from openapi_client.models.search_type_enum import SearchTypeEnum

class CatalogProductOfferingsRequestAir(CatalogProductOfferingsRequest):
    """
    CatalogProductOfferingsRequestAir
    """
    max_number_of_offers_to_return: Optional[conint(strict=True, ge=0)] = Field(None, alias="maxNumberOfOffersToReturn", description="This attribute is deprecated and not validated if sent")
    offers_per_page: Optional[conint(strict=True, ge=0)] = Field(None, alias="offersPerPage", description="Number of offers per page")
    content_source_list: Optional[conlist(ContentSourceEnum)] = Field(None, alias="contentSourceList")
    max_number_of_upsells_to_return: Optional[conint(strict=True, ge=0)] = Field(None, alias="maxNumberOfUpsellsToReturn", description="The maximum number of upsells to return")
    number_of_downsells_to_return: Optional[conint(strict=True, ge=0)] = Field(None, alias="numberOfDownsellsToReturn", description="The number of downsells to return")
    passenger_criteria: Optional[conlist(PassengerCriteria, max_items=10)] = Field(None, alias="PassengerCriteria")
    search_criteria_flight: Optional[conlist(SearchCriteriaFlight, max_items=20)] = Field(None, alias="SearchCriteriaFlight")
    search_modifiers_air: Optional[SearchModifiersAir] = Field(None, alias="SearchModifiersAir")
    payment_criteria: Optional[PaymentCriteria] = Field(None, alias="PaymentCriteria")
    pricing_modifiers_air: Optional[PricingModifiersAir] = Field(None, alias="PricingModifiersAir")
    pseudo_city_info: Optional[PseudoCityInfo] = Field(None, alias="PseudoCityInfo")
    custom_response_modifiers_air: Optional[CustomResponseModifiersAir] = Field(None, alias="CustomResponseModifiersAir")
    search_type: Optional[SearchTypeEnum] = Field(None, alias="SearchType")
    inhibit_brand_content_ind: Optional[StrictBool] = Field(None, alias="inhibitBrandContentInd", description="if true, brand infromation will be supressed.")
    detail_view_ind: Optional[StrictBool] = Field(None, alias="detailViewInd", description="if true, detail view should be returned")
    exclude_mixed_brands_ind: Optional[StrictBool] = Field(None, alias="excludeMixedBrandsInd", description="If true, mixed brands will be inhibited from the response")
    __properties = ["@type", "SearchControlConsoleChannelID", "maxNumberOfOffersToReturn", "offersPerPage", "contentSourceList", "maxNumberOfUpsellsToReturn", "numberOfDownsellsToReturn", "PassengerCriteria", "SearchCriteriaFlight", "SearchModifiersAir", "PaymentCriteria", "PricingModifiersAir", "PseudoCityInfo", "CustomResponseModifiersAir", "SearchType", "inhibitBrandContentInd", "detailViewInd", "excludeMixedBrandsInd"]

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
    def from_json(cls, json_str: str) -> CatalogProductOfferingsRequestAir:
        """Create an instance of CatalogProductOfferingsRequestAir from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of search_control_console_channel_id
        if self.search_control_console_channel_id:
            _dict['SearchControlConsoleChannelID'] = self.search_control_console_channel_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in passenger_criteria (list)
        _items = []
        if self.passenger_criteria:
            for _item in self.passenger_criteria:
                if _item:
                    _items.append(_item.to_dict())
            _dict['PassengerCriteria'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in search_criteria_flight (list)
        _items = []
        if self.search_criteria_flight:
            for _item in self.search_criteria_flight:
                if _item:
                    _items.append(_item.to_dict())
            _dict['SearchCriteriaFlight'] = _items
        # override the default output from pydantic by calling `to_dict()` of search_modifiers_air
        if self.search_modifiers_air:
            _dict['SearchModifiersAir'] = self.search_modifiers_air.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_criteria
        if self.payment_criteria:
            _dict['PaymentCriteria'] = self.payment_criteria.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pricing_modifiers_air
        if self.pricing_modifiers_air:
            _dict['PricingModifiersAir'] = self.pricing_modifiers_air.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pseudo_city_info
        if self.pseudo_city_info:
            _dict['PseudoCityInfo'] = self.pseudo_city_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_response_modifiers_air
        if self.custom_response_modifiers_air:
            _dict['CustomResponseModifiersAir'] = self.custom_response_modifiers_air.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CatalogProductOfferingsRequestAir:
        """Create an instance of CatalogProductOfferingsRequestAir from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CatalogProductOfferingsRequestAir.parse_obj(obj)

        _obj = CatalogProductOfferingsRequestAir.parse_obj({
            "type": obj.get("@type"),
            "search_control_console_channel_id": SearchControlConsoleChannelID.from_dict(obj.get("SearchControlConsoleChannelID")) if obj.get("SearchControlConsoleChannelID") is not None else None,
            "max_number_of_offers_to_return": obj.get("maxNumberOfOffersToReturn"),
            "offers_per_page": obj.get("offersPerPage"),
            "content_source_list": obj.get("contentSourceList"),
            "max_number_of_upsells_to_return": obj.get("maxNumberOfUpsellsToReturn"),
            "number_of_downsells_to_return": obj.get("numberOfDownsellsToReturn"),
            "passenger_criteria": [PassengerCriteria.from_dict(_item) for _item in obj.get("PassengerCriteria")] if obj.get("PassengerCriteria") is not None else None,
            "search_criteria_flight": [SearchCriteriaFlight.from_dict(_item) for _item in obj.get("SearchCriteriaFlight")] if obj.get("SearchCriteriaFlight") is not None else None,
            "search_modifiers_air": SearchModifiersAir.from_dict(obj.get("SearchModifiersAir")) if obj.get("SearchModifiersAir") is not None else None,
            "payment_criteria": PaymentCriteria.from_dict(obj.get("PaymentCriteria")) if obj.get("PaymentCriteria") is not None else None,
            "pricing_modifiers_air": PricingModifiersAir.from_dict(obj.get("PricingModifiersAir")) if obj.get("PricingModifiersAir") is not None else None,
            "pseudo_city_info": PseudoCityInfo.from_dict(obj.get("PseudoCityInfo")) if obj.get("PseudoCityInfo") is not None else None,
            "custom_response_modifiers_air": CustomResponseModifiersAir.from_dict(obj.get("CustomResponseModifiersAir")) if obj.get("CustomResponseModifiersAir") is not None else None,
            "search_type": obj.get("SearchType"),
            "inhibit_brand_content_ind": obj.get("inhibitBrandContentInd"),
            "detail_view_ind": obj.get("detailViewInd"),
            "exclude_mixed_brands_ind": obj.get("excludeMixedBrandsInd")
        })
        return _obj

