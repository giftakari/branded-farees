# EMDListResponseWrapper


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emd_list_response** | [**EMDListResponse**](EMDListResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.emd_list_response_wrapper import EMDListResponseWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of EMDListResponseWrapper from a JSON string
emd_list_response_wrapper_instance = EMDListResponseWrapper.from_json(json)
# print the JSON string representation of the object
print EMDListResponseWrapper.to_json()

# convert the object into a dict
emd_list_response_wrapper_dict = emd_list_response_wrapper_instance.to_dict()
# create an instance of EMDListResponseWrapper from a dict
emd_list_response_wrapper_form_dict = emd_list_response_wrapper.from_dict(emd_list_response_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


