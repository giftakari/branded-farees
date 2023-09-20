# ReceiptListResponseWrapper


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**receipt_list_response** | [**ReceiptListResponse**](ReceiptListResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.receipt_list_response_wrapper import ReceiptListResponseWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiptListResponseWrapper from a JSON string
receipt_list_response_wrapper_instance = ReceiptListResponseWrapper.from_json(json)
# print the JSON string representation of the object
print ReceiptListResponseWrapper.to_json()

# convert the object into a dict
receipt_list_response_wrapper_dict = receipt_list_response_wrapper_instance.to_dict()
# create an instance of ReceiptListResponseWrapper from a dict
receipt_list_response_wrapper_form_dict = receipt_list_response_wrapper.from_dict(receipt_list_response_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


