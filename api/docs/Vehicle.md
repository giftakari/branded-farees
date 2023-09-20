# Vehicle


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**baggage_quantity** | **int** | Baggage Quantity that is able to fit into the car with passengers | [optional] 
**passenger_quantity** | **str** |  | [optional] 
**door_count** | **str** | The number of doors for the vehicle | [optional] 
**image** | [**Image**](Image.md) |  | [optional] 
**vehicle_make_model** | [**VehicleMakeModel**](VehicleMakeModel.md) |  | [optional] 
**transmission_type_code** | [**Code**](Code.md) |  | [optional] 
**vehicle_category_code** | [**Code**](Code.md) |  | [optional] 
**fuel_type_code** | [**Code**](Code.md) |  | [optional] 
**vehicle_size_code** | [**Code**](Code.md) |  | [optional] 
**vehicle_class_code** | [**Code**](Code.md) |  | [optional] 
**air_conditioning_ind** | **bool** | True if vehicle has air conditioning | [optional] 

## Example

```python
from openapi_client.models.vehicle import Vehicle

# TODO update the JSON string below
json = "{}"
# create an instance of Vehicle from a JSON string
vehicle_instance = Vehicle.from_json(json)
# print the JSON string representation of the object
print Vehicle.to_json()

# convert the object into a dict
vehicle_dict = vehicle_instance.to_dict()
# create an instance of Vehicle from a dict
vehicle_form_dict = vehicle.from_dict(vehicle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


