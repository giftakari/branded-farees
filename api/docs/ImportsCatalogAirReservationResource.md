# ImportsCatalogAirReservationResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** | Local indentifier within a given message for this object. | [optional] 
**terms_and_conditions_ref** | **str** | Used to reference another instance of this object in the same message. | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 
**expiry_date** | **datetime** | The data and time the offer will expire | [optional] 
**customer_loyalty** | [**List[CustomerLoyalty]**](CustomerLoyalty.md) |  | [optional] 
**text_block** | [**List[TextBlock]**](TextBlock.md) |  | [optional] 
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
**product_ref** | **str** | Used to reference another instance of this object in the same message | [optional] 
**quantity** | **int** | The quantity of the product | [optional] 
**total_duration** | **str** | Total duration of all Segments that are part of this ProductAir | [optional] 
**flight_segment** | [**List[FlightSegment]**](FlightSegment.md) |  | 
**passenger_flight** | [**List[PassengerFlight]**](PassengerFlight.md) |  | 
**amount** | [**Amount**](Amount.md) |  | [optional] 
**commission** | [**Commission**](Commission.md) |  | [optional] 
**quantity** | **int** | The quantity value | [optional] 
**requested_passenger_type** | **str** | The requested passenger type code | [optional] 
**filed_amount** | [**FiledAmount**](FiledAmount.md) |  | [optional] 
**discount** | [**Discount**](Discount.md) |  | [optional] 
**net_fare_info** | [**NetFareInfo**](NetFareInfo.md) |  | [optional] 
**traveler_identifier_ref** | [**TravelerIdentifierRef**](TravelerIdentifierRef.md) |  | [optional] 
**net_base_amount** | [**FiledAmount**](FiledAmount.md) |  | [optional] 
**fare_calculation** | **str** |  | [optional] 
**surcharges** | [**Surcharges**](Surcharges.md) |  | [optional] 
**passenger_type_codes** | **List[str]** | List of passenger type codes | [optional] 
**baggage_type** | [**BaggageTypeEnum**](BaggageTypeEnum.md) |  | [optional] 
**product_ref** | **List[str]** | A product is any product, service or package of products and services  that can be priced and purchased by a specific supplier. | [optional] 
**baggage_item** | [**List[BaggageItem]**](BaggageItem.md) |  | [optional] 
**segment_sequence_list** | **List[int]** | Segment sequence is only to be used when the baggage allowance differs between segments within a product. If so, then the ProducRef must be specified. | [optional] 
**text** | **List[str]** |  | [optional] 
**url** | **str** | Url for the airline&#39;s baggage information web site | [optional] 

## Example

```python
from openapi_client.models.imports_catalog_air_reservation_resource import ImportsCatalogAirReservationResource

# TODO update the JSON string below
json = "{}"
# create an instance of ImportsCatalogAirReservationResource from a JSON string
imports_catalog_air_reservation_resource_instance = ImportsCatalogAirReservationResource.from_json(json)
# print the JSON string representation of the object
print ImportsCatalogAirReservationResource.to_json()

# convert the object into a dict
imports_catalog_air_reservation_resource_dict = imports_catalog_air_reservation_resource_instance.to_dict()
# create an instance of ImportsCatalogAirReservationResource from a dict
imports_catalog_air_reservation_resource_form_dict = imports_catalog_air_reservation_resource.from_dict(imports_catalog_air_reservation_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


