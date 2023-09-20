# Accounting


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** | Accounting data type | [optional] 
**template** | **str** | Accounting template | [optional] 
**name_value_pair** | [**List[NameValuePair]**](NameValuePair.md) |  | [optional] 

## Example

```python
from openapi_client.models.accounting import Accounting

# TODO update the JSON string below
json = "{}"
# create an instance of Accounting from a JSON string
accounting_instance = Accounting.from_json(json)
# print the JSON string representation of the object
print Accounting.to_json()

# convert the object into a dict
accounting_dict = accounting_instance.to_dict()
# create an instance of Accounting from a dict
accounting_form_dict = accounting.from_dict(accounting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


