# ApplicationLimit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**ApplicableLevelEnum**](ApplicableLevelEnum.md) |  | [optional] 
**start** | **str** | The start value | [optional] 
**end** | **str** | The end value | [optional] 

## Example

```python
from openapi_client.models.application_limit import ApplicationLimit

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationLimit from a JSON string
application_limit_instance = ApplicationLimit.from_json(json)
# print the JSON string representation of the object
print ApplicationLimit.to_json()

# convert the object into a dict
application_limit_dict = application_limit_instance.to_dict()
# create an instance of ApplicationLimit from a dict
application_limit_form_dict = application_limit.from_dict(application_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


