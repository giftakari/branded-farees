# FormOfPayment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**FormOfPaymentTypeEnum**](FormOfPaymentTypeEnum.md) |  | [optional] 
**document_number** | **str** | Payment document number | [optional] 
**encrypted_value** | **str** | Encrypted value | [optional] 
**document_issuer** | **str** | Document issuer | [optional] 
**document_type** | [**DocumentTypeEnum**](DocumentTypeEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.form_of_payment import FormOfPayment

# TODO update the JSON string below
json = "{}"
# create an instance of FormOfPayment from a JSON string
form_of_payment_instance = FormOfPayment.from_json(json)
# print the JSON string representation of the object
print FormOfPayment.to_json()

# convert the object into a dict
form_of_payment_dict = form_of_payment_instance.to_dict()
# create an instance of FormOfPayment from a dict
form_of_payment_form_dict = form_of_payment.from_dict(form_of_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


