# HotelPenalty


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**subject_to_tax** | [**YesNoUnknownEnum**](YesNoUnknownEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.hotel_penalty import HotelPenalty

# TODO update the JSON string below
json = "{}"
# create an instance of HotelPenalty from a JSON string
hotel_penalty_instance = HotelPenalty.from_json(json)
# print the JSON string representation of the object
print HotelPenalty.to_json()

# convert the object into a dict
hotel_penalty_dict = hotel_penalty_instance.to_dict()
# create an instance of HotelPenalty from a dict
hotel_penalty_form_dict = hotel_penalty.from_dict(hotel_penalty_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


