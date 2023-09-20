# StopoverCharge


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **str** | The ID of the stopoverCharge | 
**quantity** | **int** | The quantity of stopovers permitted at this charge | 
**amount** | [**CurrencyAmount**](CurrencyAmount.md) |  | 
**alternative_amount** | [**CurrencyAmount**](CurrencyAmount.md) |  | [optional] 

## Example

```python
from openapi_client.models.stopover_charge import StopoverCharge

# TODO update the JSON string below
json = "{}"
# create an instance of StopoverCharge from a JSON string
stopover_charge_instance = StopoverCharge.from_json(json)
# print the JSON string representation of the object
print StopoverCharge.to_json()

# convert the object into a dict
stopover_charge_dict = stopover_charge_instance.to_dict()
# create an instance of StopoverCharge from a dict
stopover_charge_form_dict = stopover_charge.from_dict(stopover_charge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


