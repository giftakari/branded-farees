# SpecificFlightCriteria


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**carrier** | **str** | Carrier | 
**flight_number** | **str** | Flight Number | 
**departure_date** | **date** | date of departure | 
**departure_time** | **str** | The departure time in local timezone | [optional] 
**arrival_date** | **date** | Arrival date | [optional] 
**arrival_time** | **str** | The arrival time in local timezone | [optional] 
**var_from** | **str** | From Airport Code IATA | 
**to** | **str** | to Airpor Code IATA | 
**cabin** | [**CabinAirEnum**](CabinAirEnum.md) |  | [optional] 
**class_of_service** | **str** | The class of service | [optional] 
**brand_tier** | **int** | Brand tier | [optional] 
**segment_sequence** | **int** | Segment sequence | 
**availability_source_code** | [**AvailabilitySourceCodeENUM**](AvailabilitySourceCodeENUM.md) |  | [optional] 
**content_source** | [**ContentSourceEnum**](ContentSourceEnum.md) |  | [optional] 
**bound_flights_ind** | **bool** | if true indicates that the flight availability was polled (availability check) using connecting segments. If false, flights were polled as point to point segments. | [optional] 

## Example

```python
from openapi_client.models.specific_flight_criteria import SpecificFlightCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of SpecificFlightCriteria from a JSON string
specific_flight_criteria_instance = SpecificFlightCriteria.from_json(json)
# print the JSON string representation of the object
print SpecificFlightCriteria.to_json()

# convert the object into a dict
specific_flight_criteria_dict = specific_flight_criteria_instance.to_dict()
# create an instance of SpecificFlightCriteria from a dict
specific_flight_criteria_form_dict = specific_flight_criteria.from_dict(specific_flight_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


