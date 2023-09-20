# SpecialServiceListRequest

supports sending a list of SpecialService objects

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**special_service** | [**List[SpecialService]**](SpecialService.md) |  | 

## Example

```python
from openapi_client.models.special_service_list_request import SpecialServiceListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialServiceListRequest from a JSON string
special_service_list_request_instance = SpecialServiceListRequest.from_json(json)
# print the JSON string representation of the object
print SpecialServiceListRequest.to_json()

# convert the object into a dict
special_service_list_request_dict = special_service_list_request_instance.to_dict()
# create an instance of SpecialServiceListRequest from a dict
special_service_list_request_form_dict = special_service_list_request.from_dict(special_service_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


