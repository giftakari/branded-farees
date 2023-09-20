# FormOfPaymentPaymentCard


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_card** | [**PaymentCard**](PaymentCard.md) |  | [optional] 
**inhibit_payment_card_authorization_ind** | **bool** | If true, the payment card will not go through card authorization process | [optional] 
**extended_payment** | [**ExtendedPayment**](ExtendedPayment.md) |  | [optional] 

## Example

```python
from openapi_client.models.form_of_payment_payment_card import FormOfPaymentPaymentCard

# TODO update the JSON string below
json = "{}"
# create an instance of FormOfPaymentPaymentCard from a JSON string
form_of_payment_payment_card_instance = FormOfPaymentPaymentCard.from_json(json)
# print the JSON string representation of the object
print FormOfPaymentPaymentCard.to_json()

# convert the object into a dict
form_of_payment_payment_card_dict = form_of_payment_payment_card_instance.to_dict()
# create an instance of FormOfPaymentPaymentCard from a dict
form_of_payment_payment_card_form_dict = form_of_payment_payment_card.from_dict(form_of_payment_payment_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


