# PriceBreakdownVehiclePrice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vehicle_price** | [**VehiclePrice**](VehiclePrice.md) |  | 
**rate_guaranteed_ind** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.price_breakdown_vehicle_price import PriceBreakdownVehiclePrice

# TODO update the JSON string below
json = "{}"
# create an instance of PriceBreakdownVehiclePrice from a JSON string
price_breakdown_vehicle_price_instance = PriceBreakdownVehiclePrice.from_json(json)
# print the JSON string representation of the object
print PriceBreakdownVehiclePrice.to_json()

# convert the object into a dict
price_breakdown_vehicle_price_dict = price_breakdown_vehicle_price_instance.to_dict()
# create an instance of PriceBreakdownVehiclePrice from a dict
price_breakdown_vehicle_price_form_dict = price_breakdown_vehicle_price.from_dict(price_breakdown_vehicle_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


