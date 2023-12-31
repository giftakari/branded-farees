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
from pydantic import Field, StrictBool, StrictStr, conlist
from openapi_client.models.identifier import Identifier
from openapi_client.models.offer_id import OfferID
from openapi_client.models.price import Price
from openapi_client.models.product_id import ProductID
from openapi_client.models.terms_and_conditions_full import TermsAndConditionsFull

class Offer(OfferID):
    """
    Offer
    """
    parent_offer_ref: Optional[StrictStr] = Field(None, alias="parentOfferRef", description="A reference to the Offer this offer is sold in conjunction with")
    product: conlist(ProductID, max_items=100, min_items=1) = Field(..., alias="Product")
    price: Price = Field(..., alias="Price")
    terms_and_conditions_full: conlist(TermsAndConditionsFull, max_items=100, min_items=1) = Field(..., alias="TermsAndConditionsFull")
    passive_offer_ind: Optional[StrictBool] = Field(None, alias="passiveOfferInd", description="If true, the Offer is passive for booking purposes.")
    __properties = ["@type", "id", "offerRef", "Identifier", "parentOfferRef", "Product", "Price", "TermsAndConditionsFull", "passiveOfferInd"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    # JSON field name that stores the object type
    __discriminator_property_name = '@type'

    # discriminator mappings
    __discriminator_value_class_map = {
        'OfferModify': 'OfferModify',
        'OfferUpsell': 'OfferUpsell'
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
    def from_json(cls, json_str: str) -> Union(OfferModify, OfferUpsell):
        """Create an instance of Offer from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in product (list)
        _items = []
        if self.product:
            for _item in self.product:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Product'] = _items
        # override the default output from pydantic by calling `to_dict()` of price
        if self.price:
            _dict['Price'] = self.price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in terms_and_conditions_full (list)
        _items = []
        if self.terms_and_conditions_full:
            for _item in self.terms_and_conditions_full:
                if _item:
                    _items.append(_item.to_dict())
            _dict['TermsAndConditionsFull'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Union(OfferModify, OfferUpsell):
        """Create an instance of Offer from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("Offer failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

from openapi_client.models.offer_modify import OfferModify
from openapi_client.models.offer_upsell import OfferUpsell
Offer.update_forward_refs()

