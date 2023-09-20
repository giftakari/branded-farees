# TravelerListRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**traveler** | [**List[Traveler]**](Traveler.md) |  | 

## Example

```python
from openapi_client.models.traveler_list_request import TravelerListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TravelerListRequest from a JSON string
traveler_list_request_instance = TravelerListRequest.from_json(json)
# print the JSON string representation of the object
print TravelerListRequest.to_json()

# convert the object into a dict
traveler_list_request_dict = traveler_list_request_instance.to_dict()
# create an instance of TravelerListRequest from a dict
traveler_list_request_form_dict = traveler_list_request.from_dict(traveler_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


