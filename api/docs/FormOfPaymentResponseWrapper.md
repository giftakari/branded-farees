# FormOfPaymentResponseWrapper


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**form_of_payment_response** | [**FormOfPaymentResponse**](FormOfPaymentResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.form_of_payment_response_wrapper import FormOfPaymentResponseWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FormOfPaymentResponseWrapper from a JSON string
form_of_payment_response_wrapper_instance = FormOfPaymentResponseWrapper.from_json(json)
# print the JSON string representation of the object
print FormOfPaymentResponseWrapper.to_json()

# convert the object into a dict
form_of_payment_response_wrapper_dict = form_of_payment_response_wrapper_instance.to_dict()
# create an instance of FormOfPaymentResponseWrapper from a dict
form_of_payment_response_wrapper_form_dict = form_of_payment_response_wrapper.from_dict(form_of_payment_response_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


