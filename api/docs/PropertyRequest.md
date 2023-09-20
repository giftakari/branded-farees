# PropertyRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**more_rates_token** | **str** | More rates token | [optional] 
**property_key** | [**PropertyKey**](PropertyKey.md) |  | 

## Example

```python
from openapi_client.models.property_request import PropertyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyRequest from a JSON string
property_request_instance = PropertyRequest.from_json(json)
# print the JSON string representation of the object
print PropertyRequest.to_json()

# convert the object into a dict
property_request_dict = property_request_instance.to_dict()
# create an instance of PropertyRequest from a dict
property_request_form_dict = property_request.from_dict(property_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


