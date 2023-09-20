# Deadline


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**specific_date** | [**DateOrDateWindows**](DateOrDateWindows.md) |  | 
**time** | **str** | Local time of the property | [optional] 

## Example

```python
from openapi_client.models.deadline import Deadline

# TODO update the JSON string below
json = "{}"
# create an instance of Deadline from a JSON string
deadline_instance = Deadline.from_json(json)
# print the JSON string representation of the object
print Deadline.to_json()

# convert the object into a dict
deadline_dict = deadline_instance.to_dict()
# create an instance of Deadline from a dict
deadline_form_dict = deadline.from_dict(deadline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


