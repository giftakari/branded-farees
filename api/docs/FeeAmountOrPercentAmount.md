# FeeAmountOrPercentAmount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**CurrencyAmount**](CurrencyAmount.md) |  | [optional] 

## Example

```python
from openapi_client.models.fee_amount_or_percent_amount import FeeAmountOrPercentAmount

# TODO update the JSON string below
json = "{}"
# create an instance of FeeAmountOrPercentAmount from a JSON string
fee_amount_or_percent_amount_instance = FeeAmountOrPercentAmount.from_json(json)
# print the JSON string representation of the object
print FeeAmountOrPercentAmount.to_json()

# convert the object into a dict
fee_amount_or_percent_amount_dict = fee_amount_or_percent_amount_instance.to_dict()
# create an instance of FeeAmountOrPercentAmount from a dict
fee_amount_or_percent_amount_form_dict = fee_amount_or_percent_amount.from_dict(fee_amount_or_percent_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


