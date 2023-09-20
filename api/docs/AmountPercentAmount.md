# AmountPercentAmount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**CurrencyAmount**](CurrencyAmount.md) |  | [optional] 

## Example

```python
from openapi_client.models.amount_percent_amount import AmountPercentAmount

# TODO update the JSON string below
json = "{}"
# create an instance of AmountPercentAmount from a JSON string
amount_percent_amount_instance = AmountPercentAmount.from_json(json)
# print the JSON string representation of the object
print AmountPercentAmount.to_json()

# convert the object into a dict
amount_percent_amount_dict = amount_percent_amount_instance.to_dict()
# create an instance of AmountPercentAmount from a dict
amount_percent_amount_form_dict = amount_percent_amount.from_dict(amount_percent_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


