# FormOfPaymentDocument


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_number** | [**DocumentNumber**](DocumentNumber.md) |  | [optional] 

## Example

```python
from openapi_client.models.form_of_payment_document import FormOfPaymentDocument

# TODO update the JSON string below
json = "{}"
# create an instance of FormOfPaymentDocument from a JSON string
form_of_payment_document_instance = FormOfPaymentDocument.from_json(json)
# print the JSON string representation of the object
print FormOfPaymentDocument.to_json()

# convert the object into a dict
form_of_payment_document_dict = form_of_payment_document_instance.to_dict()
# create an instance of FormOfPaymentDocument from a dict
form_of_payment_document_form_dict = form_of_payment_document.from_dict(form_of_payment_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


