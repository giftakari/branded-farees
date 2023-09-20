# OperationTimes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**days_of_week** | [**List[DayOfWeekEnum]**](DayOfWeekEnum.md) |  | [optional] 
**open_time** | **str** |  | [optional] 
**close_time** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.operation_times import OperationTimes

# TODO update the JSON string below
json = "{}"
# create an instance of OperationTimes from a JSON string
operation_times_instance = OperationTimes.from_json(json)
# print the JSON string representation of the object
print OperationTimes.to_json()

# convert the object into a dict
operation_times_dict = operation_times_instance.to_dict()
# create an instance of OperationTimes from a dict
operation_times_form_dict = operation_times.from_dict(operation_times_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


