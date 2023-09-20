# MinimumStayApplies


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**must_include_day_of_week** | [**DayOfWeekEnum**](DayOfWeekEnum.md) |  | [optional] 
**origin_day_of_week** | [**DayOfWeekEnum**](DayOfWeekEnum.md) |  | [optional] 
**return_time** | **str** | Return time | [optional] 
**duration** | **str** | Minimum duration | 

## Example

```python
from openapi_client.models.minimum_stay_applies import MinimumStayApplies

# TODO update the JSON string below
json = "{}"
# create an instance of MinimumStayApplies from a JSON string
minimum_stay_applies_instance = MinimumStayApplies.from_json(json)
# print the JSON string representation of the object
print MinimumStayApplies.to_json()

# convert the object into a dict
minimum_stay_applies_dict = minimum_stay_applies_instance.to_dict()
# create an instance of MinimumStayApplies from a dict
minimum_stay_applies_form_dict = minimum_stay_applies.from_dict(minimum_stay_applies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


