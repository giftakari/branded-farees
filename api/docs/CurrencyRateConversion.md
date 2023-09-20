# CurrencyRateConversion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**source_currency** | [**CurrencyCode**](CurrencyCode.md) |  | 
**target_currency** | [**CurrencyCode**](CurrencyCode.md) |  | 
**conversion_rate** | [**ConversionRate**](ConversionRate.md) |  | 

## Example

```python
from openapi_client.models.currency_rate_conversion import CurrencyRateConversion

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyRateConversion from a JSON string
currency_rate_conversion_instance = CurrencyRateConversion.from_json(json)
# print the JSON string representation of the object
print CurrencyRateConversion.to_json()

# convert the object into a dict
currency_rate_conversion_dict = currency_rate_conversion_instance.to_dict()
# create an instance of CurrencyRateConversion from a dict
currency_rate_conversion_form_dict = currency_rate_conversion.from_dict(currency_rate_conversion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


