# ReceiptQueryBuildFromPayment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment** | [**PaymentID**](PaymentID.md) |  | [optional] 

## Example

```python
from openapi_client.models.receipt_query_build_from_payment import ReceiptQueryBuildFromPayment

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiptQueryBuildFromPayment from a JSON string
receipt_query_build_from_payment_instance = ReceiptQueryBuildFromPayment.from_json(json)
# print the JSON string representation of the object
print ReceiptQueryBuildFromPayment.to_json()

# convert the object into a dict
receipt_query_build_from_payment_dict = receipt_query_build_from_payment_instance.to_dict()
# create an instance of ReceiptQueryBuildFromPayment from a dict
receipt_query_build_from_payment_form_dict = receipt_query_build_from_payment.from_dict(receipt_query_build_from_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


