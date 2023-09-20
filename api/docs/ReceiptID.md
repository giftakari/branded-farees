# ReceiptID


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** | The verification number. | [optional] 
**receipt_ref** | **str** |  | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.receipt_id import ReceiptID

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiptID from a JSON string
receipt_id_instance = ReceiptID.from_json(json)
# print the JSON string representation of the object
print ReceiptID.to_json()

# convert the object into a dict
receipt_id_dict = receipt_id_instance.to_dict()
# create an instance of ReceiptID from a dict
receipt_id_form_dict = receipt_id.from_dict(receipt_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


