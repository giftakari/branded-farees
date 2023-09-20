# PaymentResponseWrapper


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_response** | [**PaymentResponse**](PaymentResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_response_wrapper import PaymentResponseWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentResponseWrapper from a JSON string
payment_response_wrapper_instance = PaymentResponseWrapper.from_json(json)
# print the JSON string representation of the object
print PaymentResponseWrapper.to_json()

# convert the object into a dict
payment_response_wrapper_dict = payment_response_wrapper_instance.to_dict()
# create an instance of PaymentResponseWrapper from a dict
payment_response_wrapper_form_dict = payment_response_wrapper.from_dict(payment_response_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


