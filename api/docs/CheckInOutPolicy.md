# CheckInOutPolicy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**check_in_time** | **str** | Check-in time | 
**check_out_time** | **str** | Check-out time | 
**minimum_age** | **int** | Minimum age of guest checking in or out | [optional] 
**description** | [**List[TextTitleAndDescription]**](TextTitleAndDescription.md) |  | [optional] 

## Example

```python
from openapi_client.models.check_in_out_policy import CheckInOutPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of CheckInOutPolicy from a JSON string
check_in_out_policy_instance = CheckInOutPolicy.from_json(json)
# print the JSON string representation of the object
print CheckInOutPolicy.to_json()

# convert the object into a dict
check_in_out_policy_dict = check_in_out_policy_instance.to_dict()
# create an instance of CheckInOutPolicy from a dict
check_in_out_policy_form_dict = check_in_out_policy.from_dict(check_in_out_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


