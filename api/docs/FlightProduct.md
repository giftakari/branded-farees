# FlightProduct


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**segment_sequence** | **List[int]** | The Segment sequence | 
**class_of_service** | **str** | The class of service | [optional] 
**cabin** | [**CabinAirEnum**](CabinAirEnum.md) |  | [optional] 
**fare_basis_code** | **str** | Fare basis code | [optional] 
**fare_type** | [**FareTypeEnum**](FareTypeEnum.md) |  | [optional] 
**car_code** | **str** | The car code | [optional] 
**value_code** | **str** | The value code | [optional] 
**brand** | [**BrandID**](BrandID.md) |  | [optional] 
**customer_loyalty_credit** | [**List[CustomerLoyaltyCredit]**](CustomerLoyaltyCredit.md) |  | [optional] 
**class_of_service_availability** | [**List[ClassOfServiceAvailability]**](ClassOfServiceAvailability.md) |  | [optional] 
**fare_qualifier** | [**FareQualifierENUM**](FareQualifierENUM.md) |  | [optional] 
**stopover_priced** | [**YesNoUnknownEnum**](YesNoUnknownEnum.md) |  | [optional] 
**ticket_designator** | **str** | The ticket designator | [optional] 
**fare_type_code** | **str** | The ATPCO fare type code | [optional] 

## Example

```python
from openapi_client.models.flight_product import FlightProduct

# TODO update the JSON string below
json = "{}"
# create an instance of FlightProduct from a JSON string
flight_product_instance = FlightProduct.from_json(json)
# print the JSON string representation of the object
print FlightProduct.to_json()

# convert the object into a dict
flight_product_dict = flight_product_instance.to_dict()
# create an instance of FlightProduct from a dict
flight_product_form_dict = flight_product.from_dict(flight_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


