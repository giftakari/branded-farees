# HotelPenaltyPercent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applies_to** | [**PercentAppliesTo**](PercentAppliesTo.md) |  | 
**percent** | **float** | A percentage charged as a Penalty | 
**nights** | **int** | The number of nights the percentage needs to be applied to determine cancel penalty amount | [optional] 
**amount** | [**List[CurrencyAmount]**](CurrencyAmount.md) |  | [optional] 

## Example

```python
from openapi_client.models.hotel_penalty_percent import HotelPenaltyPercent

# TODO update the JSON string below
json = "{}"
# create an instance of HotelPenaltyPercent from a JSON string
hotel_penalty_percent_instance = HotelPenaltyPercent.from_json(json)
# print the JSON string representation of the object
print HotelPenaltyPercent.to_json()

# convert the object into a dict
hotel_penalty_percent_dict = hotel_penalty_percent_instance.to_dict()
# create an instance of HotelPenaltyPercent from a dict
hotel_penalty_percent_form_dict = hotel_penalty_percent.from_dict(hotel_penalty_percent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


