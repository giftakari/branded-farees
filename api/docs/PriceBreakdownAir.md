# PriceBreakdownAir


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** | The quantity value | [optional] 
**requested_passenger_type** | **str** | The requested passenger type code | [optional] 
**filed_amount** | [**FiledAmount**](FiledAmount.md) |  | [optional] 
**discount** | [**Discount**](Discount.md) |  | [optional] 
**net_fare_info** | [**NetFareInfo**](NetFareInfo.md) |  | [optional] 
**traveler_identifier_ref** | [**TravelerIdentifierRef**](TravelerIdentifierRef.md) |  | [optional] 
**net_base_amount** | [**FiledAmount**](FiledAmount.md) |  | [optional] 
**fare_calculation** | **str** |  | [optional] 
**surcharges** | [**Surcharges**](Surcharges.md) |  | [optional] 

## Example

```python
from openapi_client.models.price_breakdown_air import PriceBreakdownAir

# TODO update the JSON string below
json = "{}"
# create an instance of PriceBreakdownAir from a JSON string
price_breakdown_air_instance = PriceBreakdownAir.from_json(json)
# print the JSON string representation of the object
print PriceBreakdownAir.to_json()

# convert the object into a dict
price_breakdown_air_dict = price_breakdown_air_instance.to_dict()
# create an instance of PriceBreakdownAir from a dict
price_breakdown_air_form_dict = price_breakdown_air.from_dict(price_breakdown_air_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


