# FormOfPaymentInvoice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_number** | **str** | The invoice number applicable to this form of payment. Send null or empty string if no invoice number specified. | [optional] 

## Example

```python
from openapi_client.models.form_of_payment_invoice import FormOfPaymentInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of FormOfPaymentInvoice from a JSON string
form_of_payment_invoice_instance = FormOfPaymentInvoice.from_json(json)
# print the JSON string representation of the object
print FormOfPaymentInvoice.to_json()

# convert the object into a dict
form_of_payment_invoice_dict = form_of_payment_invoice_instance.to_dict()
# create an instance of FormOfPaymentInvoice from a dict
form_of_payment_invoice_form_dict = form_of_payment_invoice.from_dict(form_of_payment_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


