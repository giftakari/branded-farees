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
from pydantic import Field
from openapi_client.models.address import Address
from openapi_client.models.doc_type_code_enum import DocTypeCodeEnum
from openapi_client.models.gender_enum import GenderEnum
from openapi_client.models.geo_political_area import GeoPoliticalArea
from openapi_client.models.person_name import PersonName
from openapi_client.models.travel_document import TravelDocument

class TravelDocumentDetail(TravelDocument):
    """
    TravelDocumentDetail
    """
    issued_for_geo_political_area: Optional[GeoPoliticalArea] = Field(None, alias="IssuedForGeoPoliticalArea")
    address: Optional[Address] = Field(None, alias="Address")
    __properties = ["@type", "docNumber", "docType", "issueDate", "expireDate", "stateProvCode", "placeOfIssue", "issueCountry", "birthDate", "birthCountry", "birthPlace", "residence", "id", "Gender", "Nationality", "PersonName", "IssuedForGeoPoliticalArea", "Address"]

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
    def from_json(cls, json_str: str) -> TravelDocumentDetail:
        """Create an instance of TravelDocumentDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of person_name
        if self.person_name:
            _dict['PersonName'] = self.person_name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of issued_for_geo_political_area
        if self.issued_for_geo_political_area:
            _dict['IssuedForGeoPoliticalArea'] = self.issued_for_geo_political_area.to_dict()
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['Address'] = self.address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TravelDocumentDetail:
        """Create an instance of TravelDocumentDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TravelDocumentDetail.parse_obj(obj)

        _obj = TravelDocumentDetail.parse_obj({
            "type": obj.get("@type"),
            "doc_number": obj.get("docNumber"),
            "doc_type": obj.get("docType"),
            "issue_date": obj.get("issueDate"),
            "expire_date": obj.get("expireDate"),
            "state_prov_code": obj.get("stateProvCode"),
            "place_of_issue": obj.get("placeOfIssue"),
            "issue_country": obj.get("issueCountry"),
            "birth_date": obj.get("birthDate"),
            "birth_country": obj.get("birthCountry"),
            "birth_place": obj.get("birthPlace"),
            "residence": obj.get("residence"),
            "id": obj.get("id"),
            "gender": obj.get("Gender"),
            "nationality": obj.get("Nationality"),
            "person_name": PersonName.from_dict(obj.get("PersonName")) if obj.get("PersonName") is not None else None,
            "issued_for_geo_political_area": GeoPoliticalArea.from_dict(obj.get("IssuedForGeoPoliticalArea")) if obj.get("IssuedForGeoPoliticalArea") is not None else None,
            "address": Address.from_dict(obj.get("Address")) if obj.get("Address") is not None else None
        })
        return _obj


