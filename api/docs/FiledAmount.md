# FiledAmount

The base amount of a ticket price or net price that is filed in local currency

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | Filed amount value | [optional] 
**currency_code** | **str** | Filed amount currency code | [optional] 
**code_authority** | **str** | Filed amount currency code authority | 
**decimal_place** | **int** | ISO 4217 standard has a different number of decimals | 
**decimal_authority** | **str** | ISO 4217 standard decimal authority | [optional] 

## Example

```python
from openapi_client.models.filed_amount import FiledAmount

# TODO update the JSON string below
json = "{}"
# create an instance of FiledAmount from a JSON string
filed_amount_instance = FiledAmount.from_json(json)
# print the JSON string representation of the object
print FiledAmount.to_json()

# convert the object into a dict
filed_amount_dict = filed_amount_instance.to_dict()
# create an instance of FiledAmount from a dict
filed_amount_form_dict = filed_amount.from_dict(filed_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


