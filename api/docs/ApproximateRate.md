# ApproximateRate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**base_rate** | [**CurrencyAmount**](CurrencyAmount.md) |  | [optional] 
**rate_for_period** | [**CurrencyAmount**](CurrencyAmount.md) |  | [optional] 
**drop_off_charge** | [**CurrencyAmount**](CurrencyAmount.md) |  | [optional] 
**extra_mileage_charge** | [**CurrencyAmount**](CurrencyAmount.md) |  | [optional] 
**estimated_total_amount** | [**CurrencyAmount**](CurrencyAmount.md) |  | [optional] 

## Example

```python
from openapi_client.models.approximate_rate import ApproximateRate

# TODO update the JSON string below
json = "{}"
# create an instance of ApproximateRate from a JSON string
approximate_rate_instance = ApproximateRate.from_json(json)
# print the JSON string representation of the object
print ApproximateRate.to_json()

# convert the object into a dict
approximate_rate_dict = approximate_rate_instance.to_dict()
# create an instance of ApproximateRate from a dict
approximate_rate_form_dict = approximate_rate.from_dict(approximate_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


