# TermsAndConditionsFullAir


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baggage_allowance** | [**List[BaggageAllowance]**](BaggageAllowance.md) |  | [optional] 
**fare_rule_identifier_ref** | [**IdentifierRef**](IdentifierRef.md) |  | [optional] 
**restriction** | [**List[Restriction]**](Restriction.md) |  | [optional] 
**organization_information** | [**OrganizationInformation**](OrganizationInformation.md) |  | [optional] 
**validating_airline** | [**List[ValidatingAirline]**](ValidatingAirline.md) |  | [optional] 
**baggage_recheck** | [**List[BaggageRecheck]**](BaggageRecheck.md) |  | [optional] 
**ticketing_agency** | [**List[TicketingAgency]**](TicketingAgency.md) |  | [optional] 
**payment_time_limit** | **datetime** | The date and time by which the Offer must be paid for once the Reservation is completed | [optional] 
**promotional_code** | [**PromotionalCode**](PromotionalCode.md) |  | [optional] 
**penalties** | [**List[Penalties]**](Penalties.md) |  | [optional] 
**fare_guarantee_policy** | [**List[FareGuaranteePolicy]**](FareGuaranteePolicy.md) |  | [optional] 
**pricing_agency** | [**List[PricingAgency]**](PricingAgency.md) |  | [optional] 
**instant_purchase_ind** | **bool** | If true the Offer/Offering must be paid for at the same time as creating the Reservation | [optional] 
**secure_flight_passenger_data_required_ind** | **bool** | If true, Secure Flight Passenger Data must be input for all Travelers to complete the Reservation | [optional] 
**tour_codes** | [**List[TourCodes]**](TourCodes.md) |  | [optional] 
**document_valid_date_range** | [**DocumentValidDateRange**](DocumentValidDateRange.md) |  | [optional] 
**text_block** | [**List[TextBlock]**](TextBlock.md) |  | [optional] 

## Example

```python
from openapi_client.models.terms_and_conditions_full_air import TermsAndConditionsFullAir

# TODO update the JSON string below
json = "{}"
# create an instance of TermsAndConditionsFullAir from a JSON string
terms_and_conditions_full_air_instance = TermsAndConditionsFullAir.from_json(json)
# print the JSON string representation of the object
print TermsAndConditionsFullAir.to_json()

# convert the object into a dict
terms_and_conditions_full_air_dict = terms_and_conditions_full_air_instance.to_dict()
# create an instance of TermsAndConditionsFullAir from a dict
terms_and_conditions_full_air_form_dict = terms_and_conditions_full_air.from_dict(terms_and_conditions_full_air_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


