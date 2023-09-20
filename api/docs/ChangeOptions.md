# ChangeOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_types** | [**List[ChangeTypeENUM]**](ChangeTypeENUM.md) |  | 
**change_penalty_range** | [**ChangePenaltyRange**](ChangePenaltyRange.md) |  | [optional] 

## Example

```python
from openapi_client.models.change_options import ChangeOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeOptions from a JSON string
change_options_instance = ChangeOptions.from_json(json)
# print the JSON string representation of the object
print ChangeOptions.to_json()

# convert the object into a dict
change_options_dict = change_options_instance.to_dict()
# create an instance of ChangeOptions from a dict
change_options_form_dict = change_options.from_dict(change_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


