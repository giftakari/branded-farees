# FormOfPaymentCash


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_non_refundable_ind** | **bool** | This indicates that the Cash payment should not be refunded | [optional] 

## Example

```python
from openapi_client.models.form_of_payment_cash import FormOfPaymentCash

# TODO update the JSON string below
json = "{}"
# create an instance of FormOfPaymentCash from a JSON string
form_of_payment_cash_instance = FormOfPaymentCash.from_json(json)
# print the JSON string representation of the object
print FormOfPaymentCash.to_json()

# convert the object into a dict
form_of_payment_cash_dict = form_of_payment_cash_instance.to_dict()
# create an instance of FormOfPaymentCash from a dict
form_of_payment_cash_form_dict = form_of_payment_cash.from_dict(form_of_payment_cash_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


