# Flight


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distance** | **int** | The flight travelled distance | [optional] 
**stops** | **int** | Number of stops | [optional] 
**duration** | **str** | Elapsed flight time represented in ISO 8601 format | [optional] 
**carrier** | **str** | The airline code | 
**number** | **str** | Flight number | 
**operating_carrier** | **str** | The airline code | [optional] 
**operating_carrier_name** | **str** | The operating carrier name | [optional] 
**equipment** | **str** | Air Equip Code IATA | [optional] 
**departure** | [**Departure**](Departure.md) |  | 
**arrival** | [**Arrival**](Arrival.md) |  | 
**intermediate_stop** | [**List[IntermediateStop]**](IntermediateStop.md) |  | [optional] 
**subject_to_government_approval_ind** | **bool** | If true, this flight schedule is yet to receive government approval | [optional] 

## Example

```python
from openapi_client.models.flight import Flight

# TODO update the JSON string below
json = "{}"
# create an instance of Flight from a JSON string
flight_instance = Flight.from_json(json)
# print the JSON string representation of the object
print Flight.to_json()

# convert the object into a dict
flight_dict = flight_instance.to_dict()
# create an instance of Flight from a dict
flight_form_dict = flight.from_dict(flight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


