# Calculation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit_amount** | [**CurrencyAmount**](CurrencyAmount.md) |  | [optional] 
**unit_name** | [**RatePeriodEnum**](RatePeriodEnum.md) |  | [optional] 
**quantity** | **int** | The quantity used in the calculation of the vehicle charge e.g 2 x $500 per week | [optional] 
**max_quantity** | **int** | The maximum quantity allowed for a charge e.g Baby seat charged at $10 per day for a maximum of 10 days | [optional] 
**total_amount** | [**CurrencyAmount**](CurrencyAmount.md) |  | [optional] 
**percent** | **float** | Used when the charge is based on a percentage of a TotalAmount | [optional] 
**applicability** | [**Comment**](Comment.md) |  | [optional] 

## Example

```python
from openapi_client.models.calculation import Calculation

# TODO update the JSON string below
json = "{}"
# create an instance of Calculation from a JSON string
calculation_instance = Calculation.from_json(json)
# print the JSON string representation of the object
print Calculation.to_json()

# convert the object into a dict
calculation_dict = calculation_instance.to_dict()
# create an instance of Calculation from a dict
calculation_form_dict = calculation.from_dict(calculation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


