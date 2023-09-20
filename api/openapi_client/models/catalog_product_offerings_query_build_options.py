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



from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.build_options import BuildOptions

class CatalogProductOfferingsQueryBuildOptions(BaseModel):
    """
    CatalogProductOfferingsQueryBuildOptions
    """
    type: StrictStr = Field(..., alias="@type")
    build_options: BuildOptions = Field(..., alias="BuildOptions")
    __properties = ["@type", "BuildOptions"]

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
    def from_json(cls, json_str: str) -> CatalogProductOfferingsQueryBuildOptions:
        """Create an instance of CatalogProductOfferingsQueryBuildOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of build_options
        if self.build_options:
            _dict['BuildOptions'] = self.build_options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CatalogProductOfferingsQueryBuildOptions:
        """Create an instance of CatalogProductOfferingsQueryBuildOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CatalogProductOfferingsQueryBuildOptions.parse_obj(obj)

        _obj = CatalogProductOfferingsQueryBuildOptions.parse_obj({
            "type": obj.get("@type"),
            "build_options": BuildOptions.from_dict(obj.get("BuildOptions")) if obj.get("BuildOptions") is not None else None
        })
        return _obj

