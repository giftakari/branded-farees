# FormOfPaymentForfeit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forfeit_ind** | **bool** | If true, this form of payment instruction is to forfeit residual amounts specified in an Offer. Used in conjunction with Payment to specify which amounts to be forfeited | [optional] 

## Example

```python
from openapi_client.models.form_of_payment_forfeit import FormOfPaymentForfeit

# TODO update the JSON string below
json = "{}"
# create an instance of FormOfPaymentForfeit from a JSON string
form_of_payment_forfeit_instance = FormOfPaymentForfeit.from_json(json)
# print the JSON string representation of the object
print FormOfPaymentForfeit.to_json()

# convert the object into a dict
form_of_payment_forfeit_dict = form_of_payment_forfeit_instance.to_dict()
# create an instance of FormOfPaymentForfeit from a dict
form_of_payment_forfeit_form_dict = form_of_payment_forfeit.from_dict(form_of_payment_forfeit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


