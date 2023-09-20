# ReceiptPayment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_identifier** | [**PaymentIdentifier**](PaymentIdentifier.md) |  | [optional] 
**document** | [**List[Document]**](Document.md) |  | [optional] 

## Example

```python
from openapi_client.models.receipt_payment import ReceiptPayment

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiptPayment from a JSON string
receipt_payment_instance = ReceiptPayment.from_json(json)
# print the JSON string representation of the object
print ReceiptPayment.to_json()

# convert the object into a dict
receipt_payment_dict = receipt_payment_instance.to_dict()
# create an instance of ReceiptPayment from a dict
receipt_payment_form_dict = receipt_payment.from_dict(receipt_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


