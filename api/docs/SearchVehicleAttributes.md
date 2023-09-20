# SearchVehicleAttributes

The physical vehical attrirbutes that a person can search on.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transmission_type_code** | [**Code**](Code.md) |  | [optional] 
**vehicle_category_code** | [**Code**](Code.md) |  | [optional] 
**fuel_type_code** | [**Code**](Code.md) |  | [optional] 
**vehicle_size_code** | [**Code**](Code.md) |  | [optional] 
**door_count** | **str** | Number of doors | [optional] 
**air_conditioning_ind** | **bool** | True if requesting air conditioning | [optional] 

## Example

```python
from openapi_client.models.search_vehicle_attributes import SearchVehicleAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SearchVehicleAttributes from a JSON string
search_vehicle_attributes_instance = SearchVehicleAttributes.from_json(json)
# print the JSON string representation of the object
print SearchVehicleAttributes.to_json()

# convert the object into a dict
search_vehicle_attributes_dict = search_vehicle_attributes_instance.to_dict()
# create an instance of SearchVehicleAttributes from a dict
search_vehicle_attributes_form_dict = search_vehicle_attributes.from_dict(search_vehicle_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


