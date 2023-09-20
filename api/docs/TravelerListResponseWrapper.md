# TravelerListResponseWrapper


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**traveler_list_response** | [**TravelerListResponse**](TravelerListResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.traveler_list_response_wrapper import TravelerListResponseWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of TravelerListResponseWrapper from a JSON string
traveler_list_response_wrapper_instance = TravelerListResponseWrapper.from_json(json)
# print the JSON string representation of the object
print TravelerListResponseWrapper.to_json()

# convert the object into a dict
traveler_list_response_wrapper_dict = traveler_list_response_wrapper_instance.to_dict()
# create an instance of TravelerListResponseWrapper from a dict
traveler_list_response_wrapper_form_dict = traveler_list_response_wrapper.from_dict(traveler_list_response_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


