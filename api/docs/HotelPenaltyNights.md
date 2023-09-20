# HotelPenaltyNights


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nights** | **int** | The number of nights that will be charged as a penalty | 

## Example

```python
from openapi_client.models.hotel_penalty_nights import HotelPenaltyNights

# TODO update the JSON string below
json = "{}"
# create an instance of HotelPenaltyNights from a JSON string
hotel_penalty_nights_instance = HotelPenaltyNights.from_json(json)
# print the JSON string representation of the object
print HotelPenaltyNights.to_json()

# convert the object into a dict
hotel_penalty_nights_dict = hotel_penalty_nights_instance.to_dict()
# create an instance of HotelPenaltyNights from a dict
hotel_penalty_nights_form_dict = hotel_penalty_nights.from_dict(hotel_penalty_nights_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


