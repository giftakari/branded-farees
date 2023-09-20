# ReceiptCancellation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancellation** | [**Cancellation**](Cancellation.md) |  | [optional] 

## Example

```python
from openapi_client.models.receipt_cancellation import ReceiptCancellation

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiptCancellation from a JSON string
receipt_cancellation_instance = ReceiptCancellation.from_json(json)
# print the JSON string representation of the object
print ReceiptCancellation.to_json()

# convert the object into a dict
receipt_cancellation_dict = receipt_cancellation_instance.to_dict()
# create an instance of ReceiptCancellation from a dict
receipt_cancellation_form_dict = receipt_cancellation.from_dict(receipt_cancellation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


