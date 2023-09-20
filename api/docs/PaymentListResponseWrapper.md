# PaymentListResponseWrapper


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_list_response** | [**PaymentListResponse**](PaymentListResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_list_response_wrapper import PaymentListResponseWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentListResponseWrapper from a JSON string
payment_list_response_wrapper_instance = PaymentListResponseWrapper.from_json(json)
# print the JSON string representation of the object
print PaymentListResponseWrapper.to_json()

# convert the object into a dict
payment_list_response_wrapper_dict = payment_list_response_wrapper_instance.to_dict()
# create an instance of PaymentListResponseWrapper from a dict
payment_list_response_wrapper_form_dict = payment_list_response_wrapper.from_dict(payment_list_response_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


