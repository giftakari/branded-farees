# DayOfWeekDuration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**time_of_day** | **str** | The time of day indicates the earliest time the Offer can be reserved. Used in conjunction with DayOfWeek or Duration | [optional] 

## Example

```python
from openapi_client.models.day_of_week_duration import DayOfWeekDuration

# TODO update the JSON string below
json = "{}"
# create an instance of DayOfWeekDuration from a JSON string
day_of_week_duration_instance = DayOfWeekDuration.from_json(json)
# print the JSON string representation of the object
print DayOfWeekDuration.to_json()

# convert the object into a dict
day_of_week_duration_dict = day_of_week_duration_instance.to_dict()
# create an instance of DayOfWeekDuration from a dict
day_of_week_duration_form_dict = day_of_week_duration.from_dict(day_of_week_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


