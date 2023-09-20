# SearchCriteriaFlight


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**departure_date** | **date** | Preferred local departure date. Cannot be used in conjunction with arrival date | 
**departure_time** | **str** | Preferred local departure time. Cannot be used in conjunction with arrival time | [optional] 
**arrival_date** | **date** | Preferred local arrival date. Cannot be used in conjunction with departure date. | [optional] 
**arrival_time** | **str** | Preferred local arrival time. Cannot be used in conjunction with departure time. | [optional] 
**leg_sequence** | **int** | Leg sequence | [optional] 
**var_from** | [**FromTo**](FromTo.md) |  | 
**to** | [**FromTo**](FromTo.md) |  | 
**departure_time_range** | [**TimeRange**](TimeRange.md) |  | [optional] 

## Example

```python
from openapi_client.models.search_criteria_flight import SearchCriteriaFlight

# TODO update the JSON string below
json = "{}"
# create an instance of SearchCriteriaFlight from a JSON string
search_criteria_flight_instance = SearchCriteriaFlight.from_json(json)
# print the JSON string representation of the object
print SearchCriteriaFlight.to_json()

# convert the object into a dict
search_criteria_flight_dict = search_criteria_flight_instance.to_dict()
# create an instance of SearchCriteriaFlight from a dict
search_criteria_flight_form_dict = search_criteria_flight.from_dict(search_criteria_flight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


