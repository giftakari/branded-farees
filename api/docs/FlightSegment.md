# FlightSegment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **str** | Local indentifier within a given message for this object. | [optional] 
**sequence** | **int** | Segment sequence | 
**connection_duration** | **str** | The actual duration (in minutes) between | [optional] 
**flight** | [**FlightID**](FlightID.md) |  | 
**operational_status** | [**OperationalStatusENUM**](OperationalStatusENUM.md) |  | [optional] 
**bound_flights_ind** | **bool** | If present and true, the Segments in this Connection must be sold and cancelled together. | [optional] 
**co2_actual** | [**Measurement**](Measurement.md) |  | [optional] 

## Example

```python
from openapi_client.models.flight_segment import FlightSegment

# TODO update the JSON string below
json = "{}"
# create an instance of FlightSegment from a JSON string
flight_segment_instance = FlightSegment.from_json(json)
# print the JSON string representation of the object
print FlightSegment.to_json()

# convert the object into a dict
flight_segment_dict = flight_segment_instance.to_dict()
# create an instance of FlightSegment from a dict
flight_segment_form_dict = flight_segment.from_dict(flight_segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


