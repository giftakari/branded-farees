# ErrorWarningDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **str** | The identifier of the source system sending the error or warning | 
**source_code** | **str** | The error or warning code returned by the source airline or host system | [optional] 
**source_description** | **str** | The error or warning message as it is returned by the source airline or host system | [optional] 

## Example

```python
from openapi_client.models.error_warning_detail import ErrorWarningDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorWarningDetail from a JSON string
error_warning_detail_instance = ErrorWarningDetail.from_json(json)
# print the JSON string representation of the object
print ErrorWarningDetail.to_json()

# convert the object into a dict
error_warning_detail_dict = error_warning_detail_instance.to_dict()
# create an instance of ErrorWarningDetail from a dict
error_warning_detail_form_dict = error_warning_detail.from_dict(error_warning_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


