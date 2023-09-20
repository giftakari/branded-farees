# SubPolicy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**text_formatted** | [**List[TextFormatted]**](TextFormatted.md) |  | [optional] 

## Example

```python
from openapi_client.models.sub_policy import SubPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of SubPolicy from a JSON string
sub_policy_instance = SubPolicy.from_json(json)
# print the JSON string representation of the object
print SubPolicy.to_json()

# convert the object into a dict
sub_policy_dict = sub_policy_instance.to_dict()
# create an instance of SubPolicy from a dict
sub_policy_form_dict = sub_policy.from_dict(sub_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


