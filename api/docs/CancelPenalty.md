# CancelPenalty


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**deadline** | [**Deadline**](Deadline.md) |  | [optional] 
**hotel_penalty** | [**HotelPenalty**](HotelPenalty.md) |  | [optional] 
**refundable** | [**YesNoUnknownEnum**](YesNoUnknownEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.cancel_penalty import CancelPenalty

# TODO update the JSON string below
json = "{}"
# create an instance of CancelPenalty from a JSON string
cancel_penalty_instance = CancelPenalty.from_json(json)
# print the JSON string representation of the object
print CancelPenalty.to_json()

# convert the object into a dict
cancel_penalty_dict = cancel_penalty_instance.to_dict()
# create an instance of CancelPenalty from a dict
cancel_penalty_form_dict = cancel_penalty.from_dict(cancel_penalty_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


