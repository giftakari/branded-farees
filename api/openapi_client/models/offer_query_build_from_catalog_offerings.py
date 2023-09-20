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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from openapi_client.models.build_from_catalog_offerings_request import BuildFromCatalogOfferingsRequest
from openapi_client.models.cabin_preference import CabinPreference
from openapi_client.models.fare_rule_category_enum import FareRuleCategoryEnum
from openapi_client.models.fare_rule_enum import FareRuleEnum
from openapi_client.models.payment_criteria import PaymentCriteria

class OfferQueryBuildFromCatalogOfferings(BaseModel):
    """
    OfferQueryBuildFromCatalogOfferings
    """
    type: StrictStr = Field(..., alias="@type")
    build_from_catalog_offerings_request: Optional[BuildFromCatalogOfferingsRequest] = Field(None, alias="BuildFromCatalogOfferingsRequest")
    cabin_preference: Optional[CabinPreference] = Field(None, alias="CabinPreference")
    payment_criteria: Optional[PaymentCriteria] = Field(None, alias="PaymentCriteria")
    fare_rule_type: Optional[FareRuleEnum] = Field(None, alias="FareRuleType")
    fare_rule_category: Optional[conlist(FareRuleCategoryEnum, max_items=10)] = Field(None, alias="FareRuleCategory")
    low_fare_finder_ind: Optional[StrictBool] = Field(None, alias="lowFareFinderInd", description="If present and true, this is a low fare finder request")
    return_branded_fares_ind: Optional[StrictBool] = Field(None, alias="returnBrandedFaresInd", description="If present and true, branded fares are returned")
    re_check_inventory_ind: Optional[StrictBool] = Field(None, alias="reCheckInventoryInd", description="If present and true, then the host system will perform a sell inventory check.")
    validate_inventory_ind: Optional[StrictBool] = Field(None, alias="validateInventoryInd", description="If true, the flight inventory will be checked during the price step")
    __properties = ["@type", "BuildFromCatalogOfferingsRequest", "CabinPreference", "PaymentCriteria", "FareRuleType", "FareRuleCategory", "lowFareFinderInd", "returnBrandedFaresInd", "reCheckInventoryInd", "validateInventoryInd"]

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
    def from_json(cls, json_str: str) -> OfferQueryBuildFromCatalogOfferings:
        """Create an instance of OfferQueryBuildFromCatalogOfferings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of build_from_catalog_offerings_request
        if self.build_from_catalog_offerings_request:
            _dict['BuildFromCatalogOfferingsRequest'] = self.build_from_catalog_offerings_request.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cabin_preference
        if self.cabin_preference:
            _dict['CabinPreference'] = self.cabin_preference.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_criteria
        if self.payment_criteria:
            _dict['PaymentCriteria'] = self.payment_criteria.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OfferQueryBuildFromCatalogOfferings:
        """Create an instance of OfferQueryBuildFromCatalogOfferings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OfferQueryBuildFromCatalogOfferings.parse_obj(obj)

        _obj = OfferQueryBuildFromCatalogOfferings.parse_obj({
            "type": obj.get("@type"),
            "build_from_catalog_offerings_request": BuildFromCatalogOfferingsRequest.from_dict(obj.get("BuildFromCatalogOfferingsRequest")) if obj.get("BuildFromCatalogOfferingsRequest") is not None else None,
            "cabin_preference": CabinPreference.from_dict(obj.get("CabinPreference")) if obj.get("CabinPreference") is not None else None,
            "payment_criteria": PaymentCriteria.from_dict(obj.get("PaymentCriteria")) if obj.get("PaymentCriteria") is not None else None,
            "fare_rule_type": obj.get("FareRuleType"),
            "fare_rule_category": obj.get("FareRuleCategory"),
            "low_fare_finder_ind": obj.get("lowFareFinderInd"),
            "return_branded_fares_ind": obj.get("returnBrandedFaresInd"),
            "re_check_inventory_ind": obj.get("reCheckInventoryInd"),
            "validate_inventory_ind": obj.get("validateInventoryInd")
        })
        return _obj


