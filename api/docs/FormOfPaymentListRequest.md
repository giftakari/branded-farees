# FormOfPaymentListRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**form_of_payment** | [**List[FormOfPaymentID]**](FormOfPaymentID.md) |  | 

## Example

```python
from openapi_client.models.form_of_payment_list_request import FormOfPaymentListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FormOfPaymentListRequest from a JSON string
form_of_payment_list_request_instance = FormOfPaymentListRequest.from_json(json)
# print the JSON string representation of the object
print FormOfPaymentListRequest.to_json()

# convert the object into a dict
form_of_payment_list_request_dict = form_of_payment_list_request_instance.to_dict()
# create an instance of FormOfPaymentListRequest from a dict
form_of_payment_list_request_form_dict = form_of_payment_list_request.from_dict(form_of_payment_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


