# VehiclePrice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **str** | Internal ID | [optional] 
**rate_source** | **str** | Assigned Type: c-1100:StringTiny | [optional] 
**rate_guaranteed_ind** | **bool** | Assigned Type: c-1100:OptionalIndicator | [optional] 
**rate_period** | [**RatePeriodEnum**](RatePeriodEnum.md) |  | [optional] 
**rate_distance** | [**RateDistance**](RateDistance.md) |  | [optional] 
**rate_description** | [**List[TextBlock]**](TextBlock.md) |  | [optional] 
**rate_availability** | [**RateAvailabilityEnum**](RateAvailabilityEnum.md) |  | [optional] 
**supplier_rate** | [**SupplierRate**](SupplierRate.md) |  | 
**approximate_rate** | [**ApproximateRate**](ApproximateRate.md) |  | [optional] 
**customer_loyalty** | [**CustomerLoyalty**](CustomerLoyalty.md) |  | [optional] 
**rate_qualifier** | [**RateQualifierEnum**](RateQualifierEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.vehicle_price import VehiclePrice

# TODO update the JSON string below
json = "{}"
# create an instance of VehiclePrice from a JSON string
vehicle_price_instance = VehiclePrice.from_json(json)
# print the JSON string representation of the object
print VehiclePrice.to_json()

# convert the object into a dict
vehicle_price_dict = vehicle_price_instance.to_dict()
# create an instance of VehiclePrice from a dict
vehicle_price_form_dict = vehicle_price.from_dict(vehicle_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


