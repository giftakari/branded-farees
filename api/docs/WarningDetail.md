# WarningDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **str** | The identifier of the source system sending the error or warning | 
**source_code** | **str** | The error or warning code returned by the source airline or host system | [optional] 
**source_description** | **str** | The error or warning message as it is returned by the source airline or host system | [optional] 

## Example

```python
from openapi_client.models.warning_detail import WarningDetail

# TODO update the JSON string below
json = "{}"
# create an instance of WarningDetail from a JSON string
warning_detail_instance = WarningDetail.from_json(json)
# print the JSON string representation of the object
print WarningDetail.to_json()

# convert the object into a dict
warning_detail_dict = warning_detail_instance.to_dict()
# create an instance of WarningDetail from a dict
warning_detail_form_dict = warning_detail.from_dict(warning_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


