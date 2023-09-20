# DepositAmount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_amount** | [**CurrencyAmount**](CurrencyAmount.md) |  | 

## Example

```python
from openapi_client.models.deposit_amount import DepositAmount

# TODO update the JSON string below
json = "{}"
# create an instance of DepositAmount from a JSON string
deposit_amount_instance = DepositAmount.from_json(json)
# print the JSON string representation of the object
print DepositAmount.to_json()

# convert the object into a dict
deposit_amount_dict = deposit_amount_instance.to_dict()
# create an instance of DepositAmount from a dict
deposit_amount_form_dict = deposit_amount.from_dict(deposit_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


