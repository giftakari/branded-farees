# ProductListResponseWrapper


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_list_response** | [**ProductListResponse**](ProductListResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.product_list_response_wrapper import ProductListResponseWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ProductListResponseWrapper from a JSON string
product_list_response_wrapper_instance = ProductListResponseWrapper.from_json(json)
# print the JSON string representation of the object
print ProductListResponseWrapper.to_json()

# convert the object into a dict
product_list_response_wrapper_dict = product_list_response_wrapper_instance.to_dict()
# create an instance of ProductListResponseWrapper from a dict
product_list_response_wrapper_form_dict = product_list_response_wrapper.from_dict(product_list_response_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


