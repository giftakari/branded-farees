# ChangePenaltyRange


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**minimum** | [**AmountPercent**](AmountPercent.md) |  | [optional] 
**maximum** | [**AmountPercent**](AmountPercent.md) |  | [optional] 

## Example

```python
from openapi_client.models.change_penalty_range import ChangePenaltyRange

# TODO update the JSON string below
json = "{}"
# create an instance of ChangePenaltyRange from a JSON string
change_penalty_range_instance = ChangePenaltyRange.from_json(json)
# print the JSON string representation of the object
print ChangePenaltyRange.to_json()

# convert the object into a dict
change_penalty_range_dict = change_penalty_range_instance.to_dict()
# create an instance of ChangePenaltyRange from a dict
change_penalty_range_form_dict = change_penalty_range.from_dict(change_penalty_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


