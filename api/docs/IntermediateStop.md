# IntermediateStop

An intermediate stop location and duration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**arrival_flight_duration** | **str** | ArrivalFlight Duration stopped at this location | [optional] 
**departure_flight_duration** | **str** | DepartureFlight Duration stopped at this location | [optional] 
**duration** | **str** | Duration stopped at this location | [optional] 
**equipment** | **str** | Aircraft equipment. | [optional] 
**arrival_date** | **str** | The local date the aircraft arrives at the intermediate stop | [optional] 
**departure_date** | **str** | The local date the aircraft departs from the intermediate stop | [optional] 
**arrival_time** | **str** | The local time the aircraft arrives at the intermediate stop | [optional] 
**departurel_time** | **str** | The local time the aircraft departs from the intermediate stop | [optional] 
**arrival_terminal** | **str** | Arrival Terminal of the Airport | [optional] 
**departure_terminal** | **str** | Departure Terminal of the Airport | [optional] 

## Example

```python
from openapi_client.models.intermediate_stop import IntermediateStop

# TODO update the JSON string below
json = "{}"
# create an instance of IntermediateStop from a JSON string
intermediate_stop_instance = IntermediateStop.from_json(json)
# print the JSON string representation of the object
print IntermediateStop.to_json()

# convert the object into a dict
intermediate_stop_dict = intermediate_stop_instance.to_dict()
# create an instance of IntermediateStop from a dict
intermediate_stop_form_dict = intermediate_stop.from_dict(intermediate_stop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


