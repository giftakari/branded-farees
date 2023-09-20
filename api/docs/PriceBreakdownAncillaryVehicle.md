# PriceBreakdownAncillaryVehicle


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_period** | [**RatePeriodEnum**](RatePeriodEnum.md) |  | [optional] 
**pay_now_ind** | **bool** | If true the vehicle ancillary must be paid now and is included in the totalPrice calculation | [optional] 
**included_in_estimated_total_ind** | **bool** | If true the AncillaryVehicle is included in the estimated totalPrice. | [optional] 

## Example

```python
from openapi_client.models.price_breakdown_ancillary_vehicle import PriceBreakdownAncillaryVehicle

# TODO update the JSON string below
json = "{}"
# create an instance of PriceBreakdownAncillaryVehicle from a JSON string
price_breakdown_ancillary_vehicle_instance = PriceBreakdownAncillaryVehicle.from_json(json)
# print the JSON string representation of the object
print PriceBreakdownAncillaryVehicle.to_json()

# convert the object into a dict
price_breakdown_ancillary_vehicle_dict = price_breakdown_ancillary_vehicle_instance.to_dict()
# create an instance of PriceBreakdownAncillaryVehicle from a dict
price_breakdown_ancillary_vehicle_form_dict = price_breakdown_ancillary_vehicle.from_dict(price_breakdown_ancillary_vehicle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


