# ReceiptConfirmation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmation** | [**Confirmation**](Confirmation.md) |  | [optional] 
**segment_sequence_list** | **List[int]** | The segmentSequenceList the ReceiptConfirmation applies to | [optional] 

## Example

```python
from openapi_client.models.receipt_confirmation import ReceiptConfirmation

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiptConfirmation from a JSON string
receipt_confirmation_instance = ReceiptConfirmation.from_json(json)
# print the JSON string representation of the object
print ReceiptConfirmation.to_json()

# convert the object into a dict
receipt_confirmation_dict = receipt_confirmation_instance.to_dict()
# create an instance of ReceiptConfirmation from a dict
receipt_confirmation_form_dict = receipt_confirmation.from_dict(receipt_confirmation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


