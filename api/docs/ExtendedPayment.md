# ExtendedPayment

Note this field is deprecated in Payment schema and should be passed in FormOfPaymentPaymentCardExtendPayment schema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_installments** | **int** | The number of installment payments to be charged by the payment card provider | 
**first_installment** | **float** | For Pagos Parceledos, specify the first installment amount. This will be the same currency as the payment | [optional] 
**remaining_amount** | **float** | For Pagos Parceledos, specify the remaining amount to be charged that will be spread across the number of installments. This will be the same currency as the payment | [optional] 
**otato_code** | **str** | For Pagos Parceledos the OTATOCode | [optional] 

## Example

```python
from openapi_client.models.extended_payment import ExtendedPayment

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedPayment from a JSON string
extended_payment_instance = ExtendedPayment.from_json(json)
# print the JSON string representation of the object
print ExtendedPayment.to_json()

# convert the object into a dict
extended_payment_dict = extended_payment_instance.to_dict()
# create an instance of ExtendedPayment from a dict
extended_payment_form_dict = extended_payment.from_dict(extended_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


