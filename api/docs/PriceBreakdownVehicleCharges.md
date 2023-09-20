# PriceBreakdownVehicleCharges


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vehicle_charges** | [**VehicleCharges**](VehicleCharges.md) |  | [optional] 

## Example

```python
from openapi_client.models.price_breakdown_vehicle_charges import PriceBreakdownVehicleCharges

# TODO update the JSON string below
json = "{}"
# create an instance of PriceBreakdownVehicleCharges from a JSON string
price_breakdown_vehicle_charges_instance = PriceBreakdownVehicleCharges.from_json(json)
# print the JSON string representation of the object
print PriceBreakdownVehicleCharges.to_json()

# convert the object into a dict
price_breakdown_vehicle_charges_dict = price_breakdown_vehicle_charges_instance.to_dict()
# create an instance of PriceBreakdownVehicleCharges from a dict
price_breakdown_vehicle_charges_form_dict = price_breakdown_vehicle_charges.from_dict(price_breakdown_vehicle_charges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


