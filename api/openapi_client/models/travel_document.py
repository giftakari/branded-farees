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

from datetime import date
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictStr, constr, validator
from openapi_client.models.doc_type_code_enum import DocTypeCodeEnum
from openapi_client.models.gender_enum import GenderEnum
from openapi_client.models.person_name import PersonName

class TravelDocument(BaseModel):
    """
    TravelDocument
    """
    type: StrictStr = Field(..., alias="@type")
    doc_number: constr(strict=True, max_length=128) = Field(..., alias="docNumber", description="Document number value")
    doc_type: Optional[DocTypeCodeEnum] = Field(None, alias="docType")
    issue_date: Optional[date] = Field(None, alias="issueDate", description="Date of Issue")
    expire_date: Optional[date] = Field(None, alias="expireDate", description="Date of expiration")
    state_prov_code: Optional[constr(strict=True, max_length=8, min_length=2)] = Field(None, alias="stateProvCode", description="State Province Code value")
    place_of_issue: Optional[constr(strict=True, max_length=32)] = Field(None, alias="placeOfIssue", description="Place of issue value")
    issue_country: Optional[constr(strict=True)] = Field(None, alias="issueCountry", description="Issue country on Country Code ISO")
    birth_date: Optional[date] = Field(None, alias="birthDate", description="The date of birth of the document holder")
    birth_country: Optional[constr(strict=True)] = Field(None, alias="birthCountry", description="Birth country on Country Code ISO value")
    birth_place: Optional[constr(strict=True, max_length=128)] = Field(None, alias="birthPlace", description="Birth place value")
    residence: Optional[constr(strict=True, max_length=512)] = Field(None, description="Residence value")
    id: Optional[StrictStr] = Field(None, description="Locally referenced id")
    gender: GenderEnum = Field(..., alias="Gender")
    nationality: Optional[constr(strict=True)] = Field(None, alias="Nationality", description="Specifies a 2 character country code as defined in ISO3166.")
    person_name: PersonName = Field(..., alias="PersonName")
    __properties = ["@type", "docNumber", "docType", "issueDate", "expireDate", "stateProvCode", "placeOfIssue", "issueCountry", "birthDate", "birthCountry", "birthPlace", "residence", "id", "Gender", "Nationality", "PersonName"]

    @validator('issue_country')
    def issue_country_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[a-zA-Z]{2}", value):
            raise ValueError(r"must validate the regular expression /[a-zA-Z]{2}/")
        return value

    @validator('birth_country')
    def birth_country_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[a-zA-Z]{2}", value):
            raise ValueError(r"must validate the regular expression /[a-zA-Z]{2}/")
        return value

    @validator('nationality')
    def nationality_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[a-zA-Z]{2}", value):
            raise ValueError(r"must validate the regular expression /[a-zA-Z]{2}/")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    # JSON field name that stores the object type
    __discriminator_property_name = '@type'

    # discriminator mappings
    __discriminator_value_class_map = {
        'TravelDocumentDetail': 'TravelDocumentDetail'
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
    def from_json(cls, json_str: str) -> Union(TravelDocumentDetail):
        """Create an instance of TravelDocument from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Union(TravelDocumentDetail):
        """Create an instance of TravelDocument from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("TravelDocument failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

from openapi_client.models.travel_document_detail import TravelDocumentDetail
TravelDocument.update_forward_refs()

