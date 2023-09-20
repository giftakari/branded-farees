# CumulativeValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**currency_source** | [**CurrencySourceEnum**](CurrencySourceEnum.md) |  | [optional] 
**currency_code** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**base** | **float** | The price prior to all applicable taxes of a product such as the rate for a room or fare for a flight. | [optional] 
**taxes** | [**Taxes**](Taxes.md) |  | [optional] 
**fees** | [**Fees**](Fees.md) |  | [optional] 
**total** | **float** | Specifies the total price including base + taxes + fees | [optional] 
**approximate_ind** | **bool** | True if this amount has been converted from the original amount | [optional] 

## Example

```python
from openapi_client.models.cumulative_value import CumulativeValue

# TODO update the JSON string below
json = "{}"
# create an instance of CumulativeValue from a JSON string
cumulative_value_instance = CumulativeValue.from_json(json)
# print the JSON string representation of the object
print CumulativeValue.to_json()

# convert the object into a dict
cumulative_value_dict = cumulative_value_instance.to_dict()
# create an instance of CumulativeValue from a dict
cumulative_value_form_dict = cumulative_value.from_dict(cumulative_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


