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
from pydantic import Field, StrictBool, conint, constr, validator
from openapi_client.models.address import Address
from openapi_client.models.address_bldg_room import AddressBldgRoom
from openapi_client.models.address_street_number import AddressStreetNumber
from openapi_client.models.comment import Comment
from openapi_client.models.country import Country
from openapi_client.models.enum_address_role import EnumAddressRole
from openapi_client.models.privacy import Privacy
from openapi_client.models.state_prov import StateProv

class AddressDetail(Address):
    """
    AddressDetail
    """
    address_type: Optional[constr(strict=True)] = Field(None, alias="addressType", description="OTA code for address type")
    use: Optional[constr(strict=True)] = Field(None, description="OTA code for address use")
    comment: Optional[Comment] = Field(None, alias="Comment")
    privacy: Optional[Privacy] = Field(None, alias="Privacy")
    priority: Optional[conint(strict=True, le=300, ge=0)] = Field(None, alias="Priority", description="The priority ranking within the group")
    valid_ind: Optional[StrictBool] = Field(None, alias="validInd", description="If true, this is a valid and complete mailing address that has been verified through an address verification service or previously mailed materials have not been returned.")
    provisioned_ind: Optional[StrictBool] = Field(None, alias="provisionedInd", description="If true, this address came into the system through provisioning")
    __properties = ["@type", "id", "BldgRoom", "Number", "Street", "AddressLine", "City", "County", "StateProv", "Country", "PostalCode", "Addressee", "role", "addressType", "use", "Comment", "Privacy", "Priority", "validInd", "provisionedInd"]

    @validator('address_type')
    def address_type_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[0-9A-Z]{1,3}(\.[A-Z]{3}(\.X){0,1}){0,1}", value):
            raise ValueError(r"must validate the regular expression /[0-9A-Z]{1,3}(\.[A-Z]{3}(\.X){0,1}){0,1}/")
        return value

    @validator('use')
    def use_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[0-9A-Z]{1,3}(\.[A-Z]{3}(\.X){0,1}){0,1}", value):
            raise ValueError(r"must validate the regular expression /[0-9A-Z]{1,3}(\.[A-Z]{3}(\.X){0,1}){0,1}/")
        return value

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
    def from_json(cls, json_str: str) -> AddressDetail:
        """Create an instance of AddressDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of bldg_room
        if self.bldg_room:
            _dict['BldgRoom'] = self.bldg_room.to_dict()
        # override the default output from pydantic by calling `to_dict()` of number
        if self.number:
            _dict['Number'] = self.number.to_dict()
        # override the default output from pydantic by calling `to_dict()` of state_prov
        if self.state_prov:
            _dict['StateProv'] = self.state_prov.to_dict()
        # override the default output from pydantic by calling `to_dict()` of country
        if self.country:
            _dict['Country'] = self.country.to_dict()
        # override the default output from pydantic by calling `to_dict()` of comment
        if self.comment:
            _dict['Comment'] = self.comment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of privacy
        if self.privacy:
            _dict['Privacy'] = self.privacy.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AddressDetail:
        """Create an instance of AddressDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AddressDetail.parse_obj(obj)

        _obj = AddressDetail.parse_obj({
            "type": obj.get("@type"),
            "id": obj.get("id"),
            "bldg_room": AddressBldgRoom.from_dict(obj.get("BldgRoom")) if obj.get("BldgRoom") is not None else None,
            "number": AddressStreetNumber.from_dict(obj.get("Number")) if obj.get("Number") is not None else None,
            "street": obj.get("Street"),
            "address_line": obj.get("AddressLine"),
            "city": obj.get("City"),
            "county": obj.get("County"),
            "state_prov": StateProv.from_dict(obj.get("StateProv")) if obj.get("StateProv") is not None else None,
            "country": Country.from_dict(obj.get("Country")) if obj.get("Country") is not None else None,
            "postal_code": obj.get("PostalCode"),
            "addressee": obj.get("Addressee"),
            "role": obj.get("role"),
            "address_type": obj.get("addressType"),
            "use": obj.get("use"),
            "comment": Comment.from_dict(obj.get("Comment")) if obj.get("Comment") is not None else None,
            "privacy": Privacy.from_dict(obj.get("Privacy")) if obj.get("Privacy") is not None else None,
            "priority": obj.get("Priority"),
            "valid_ind": obj.get("validInd"),
            "provisioned_ind": obj.get("provisionedInd")
        })
        return _obj


