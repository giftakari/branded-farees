# TravelerResponseWrapper


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**traveler_response** | [**TravelerResponse**](TravelerResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.traveler_response_wrapper import TravelerResponseWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of TravelerResponseWrapper from a JSON string
traveler_response_wrapper_instance = TravelerResponseWrapper.from_json(json)
# print the JSON string representation of the object
print TravelerResponseWrapper.to_json()

# convert the object into a dict
traveler_response_wrapper_dict = traveler_response_wrapper_instance.to_dict()
# create an instance of TravelerResponseWrapper from a dict
traveler_response_wrapper_form_dict = traveler_response_wrapper.from_dict(traveler_response_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


