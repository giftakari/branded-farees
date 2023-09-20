# EMDListResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emdid** | [**List[EMD]**](EMD.md) |  | [optional] 

## Example

```python
from openapi_client.models.emd_list_response import EMDListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EMDListResponse from a JSON string
emd_list_response_instance = EMDListResponse.from_json(json)
# print the JSON string representation of the object
print EMDListResponse.to_json()

# convert the object into a dict
emd_list_response_dict = emd_list_response_instance.to_dict()
# create an instance of EMDListResponse from a dict
emd_list_response_form_dict = emd_list_response.from_dict(emd_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


