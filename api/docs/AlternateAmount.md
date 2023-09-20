# AlternateAmount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The base amount | 
**currency_code** | **str** | Amount currency code | 
**decimal_place** | **int** | ISO 4217 decimal standard | 
**fare_calculation** | **str** | the fare calculation string | [optional] 
**rate_of_exchange** | **float** | The rate of exchange used to convert the fare calculation | [optional] 

## Example

```python
from openapi_client.models.alternate_amount import AlternateAmount

# TODO update the JSON string below
json = "{}"
# create an instance of AlternateAmount from a JSON string
alternate_amount_instance = AlternateAmount.from_json(json)
# print the JSON string representation of the object
print AlternateAmount.to_json()

# convert the object into a dict
alternate_amount_dict = alternate_amount_instance.to_dict()
# create an instance of AlternateAmount from a dict
alternate_amount_form_dict = alternate_amount.from_dict(alternate_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


