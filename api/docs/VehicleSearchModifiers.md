# VehicleSearchModifiers


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**available_rates_only_ind** | **bool** | Assigned Type: c-1100:OptionalIndicator | [optional] 
**sellable_rates_only_ind** | **bool** | Assigned Type: c-1100:OptionalIndicator | [optional] 

## Example

```python
from openapi_client.models.vehicle_search_modifiers import VehicleSearchModifiers

# TODO update the JSON string below
json = "{}"
# create an instance of VehicleSearchModifiers from a JSON string
vehicle_search_modifiers_instance = VehicleSearchModifiers.from_json(json)
# print the JSON string representation of the object
print VehicleSearchModifiers.to_json()

# convert the object into a dict
vehicle_search_modifiers_dict = vehicle_search_modifiers_instance.to_dict()
# create an instance of VehicleSearchModifiers from a dict
vehicle_search_modifiers_form_dict = vehicle_search_modifiers.from_dict(vehicle_search_modifiers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


