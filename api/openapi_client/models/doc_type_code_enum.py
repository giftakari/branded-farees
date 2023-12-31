# coding: utf-8

"""
    Akaris Travels Air

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 11.10.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class DocTypeCodeEnum(str, Enum):
    """
    Codes from OTA DOC - Document Type
    """

    """
    allowed enum values
    """
    VISA = 'Visa'
    PASSPORT = 'Passport'
    MILITARYIDENTIFICATION = 'MilitaryIdentification'
    DRIVERSLICENSE = 'DriversLicense'
    NATIONALIDENTITYDOCUMENT = 'NationalIdentityDocument'
    VACCINATIONCERTIFICATE = 'VaccinationCertificate'
    ALIENREGISTRATIONNUMBER = 'AlienRegistrationNumber'
    INSURANCEPOLICYNUMBER = 'InsurancePolicyNumber'
    TAXEXEMPTIONNUMBER = 'TaxExemptionNumber'
    VEHICLEREGISTRATIONLICENSENUMBER = 'VehicleRegistrationLicenseNumber'
    BODERCROSSINGCARD = 'BoderCrossingCard'
    REFUGEETRAVELDOCUMENT = 'RefugeeTravelDocument'
    PILOTSLICENSE = 'PilotsLicense'
    PERMANENTRESIDENTCARD = 'PermanentResidentCard'
    REDRESSNUMBER = 'RedressNumber'
    KNOWNTRAVELERNUMBER = 'KnownTravelerNumber'
    NON_MINUS_STANDARD = 'Non-Standard'
    MERCHANTNUMBER = 'MerchantNumber'
    AIRNEXUSCARD = 'AirNexusCard'
    CREWMEMBERCERTIFICATE = 'CrewMemberCertificate'
    PASSPORTCARD = 'PassportCard'
    NATURALIZATIONCERTIFICATE = 'NaturalizationCertificate'
    TICKETNUMBER = 'TicketNumber'
    LARGEFAMILYDISCOUNTCARD = 'LargeFamilyDiscountCard'

    @classmethod
    def from_json(cls, json_str: str) -> DocTypeCodeEnum:
        """Create an instance of DocTypeCodeEnum from a JSON string"""
        return DocTypeCodeEnum(json.loads(json_str))


