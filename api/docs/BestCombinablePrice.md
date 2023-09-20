# BestCombinablePrice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** | Internally referenced id | [optional] 
**currency_code** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**base** | **float** | The total amount not including taxes and/or fees | [optional] 
**total_taxes** | **float** | The total of the taxes included in the total price | [optional] 
**total_fees** | **float** | The total of the fees included in the total price | [optional] 
**total_price** | **float** | The total price of the product in the currency indicated | [optional] 
**vendor_currency_total** | [**VendorCurrencyTotal**](VendorCurrencyTotal.md) |  | [optional] 

## Example

```python
from openapi_client.models.best_combinable_price import BestCombinablePrice

# TODO update the JSON string below
json = "{}"
# create an instance of BestCombinablePrice from a JSON string
best_combinable_price_instance = BestCombinablePrice.from_json(json)
# print the JSON string representation of the object
print BestCombinablePrice.to_json()

# convert the object into a dict
best_combinable_price_dict = best_combinable_price_instance.to_dict()
# create an instance of BestCombinablePrice from a dict
best_combinable_price_form_dict = best_combinable_price.from_dict(best_combinable_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


