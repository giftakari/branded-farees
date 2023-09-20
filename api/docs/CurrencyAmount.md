# CurrencyAmount

A monetary amount, up to 4 decimal places. Decimal place needs to be included.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | [optional] 
**code** | **str** | An ISO 4217 alpha character code that specifies a money unit | [optional] 
**minor_unit** | **int** | Minor units are a mechanism for expressing the relationship between a major currency unit and its corresponding minor currency unit. | [optional] 
**currency_source** | [**CurrencySourceEnum**](CurrencySourceEnum.md) |  | [optional] 
**approximate_ind** | **bool** | True if the currency amount has been converted from the original amount | [optional] 

## Example

```python
from openapi_client.models.currency_amount import CurrencyAmount

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyAmount from a JSON string
currency_amount_instance = CurrencyAmount.from_json(json)
# print the JSON string representation of the object
print CurrencyAmount.to_json()

# convert the object into a dict
currency_amount_dict = currency_amount_instance.to_dict()
# create an instance of CurrencyAmount from a dict
currency_amount_form_dict = currency_amount.from_dict(currency_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


