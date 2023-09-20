# AccountingID


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | [optional] 
**accounting_ref** | **str** | Accounting reference | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.accounting_id import AccountingID

# TODO update the JSON string below
json = "{}"
# create an instance of AccountingID from a JSON string
accounting_id_instance = AccountingID.from_json(json)
# print the JSON string representation of the object
print AccountingID.to_json()

# convert the object into a dict
accounting_id_dict = accounting_id_instance.to_dict()
# create an instance of AccountingID from a dict
accounting_id_form_dict = accounting_id.from_dict(accounting_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


