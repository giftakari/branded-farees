# HotelSearchCriterion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**number_of_rooms** | **int** | Number of rooms requested | [optional] 
**property_request** | [**List[PropertyRequest]**](PropertyRequest.md) |  | 
**room_stay_candidates** | [**RoomStayCandidates**](RoomStayCandidates.md) |  | [optional] 
**rate_candidates** | [**RateCandidates**](RateCandidates.md) |  | [optional] 

## Example

```python
from openapi_client.models.hotel_search_criterion import HotelSearchCriterion

# TODO update the JSON string below
json = "{}"
# create an instance of HotelSearchCriterion from a JSON string
hotel_search_criterion_instance = HotelSearchCriterion.from_json(json)
# print the JSON string representation of the object
print HotelSearchCriterion.to_json()

# convert the object into a dict
hotel_search_criterion_dict = hotel_search_criterion_instance.to_dict()
# create an instance of HotelSearchCriterion from a dict
hotel_search_criterion_form_dict = hotel_search_criterion.from_dict(hotel_search_criterion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


