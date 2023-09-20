# HotelPenaltyAmount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**includes_tax** | [**YesNoUnknownEnum**](YesNoUnknownEnum.md) |  | [optional] 
**amount** | [**List[CurrencyAmount]**](CurrencyAmount.md) |  | 

## Example

```python
from openapi_client.models.hotel_penalty_amount import HotelPenaltyAmount

# TODO update the JSON string below
json = "{}"
# create an instance of HotelPenaltyAmount from a JSON string
hotel_penalty_amount_instance = HotelPenaltyAmount.from_json(json)
# print the JSON string representation of the object
print HotelPenaltyAmount.to_json()

# convert the object into a dict
hotel_penalty_amount_dict = hotel_penalty_amount_instance.to_dict()
# create an instance of HotelPenaltyAmount from a dict
hotel_penalty_amount_form_dict = hotel_penalty_amount.from_dict(hotel_penalty_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


