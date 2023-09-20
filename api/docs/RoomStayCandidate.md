# RoomStayCandidate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guest_counts** | [**GuestCounts**](GuestCounts.md) |  | 
**room_amenity** | [**List[RoomAmenity]**](RoomAmenity.md) |  | [optional] 

## Example

```python
from openapi_client.models.room_stay_candidate import RoomStayCandidate

# TODO update the JSON string below
json = "{}"
# create an instance of RoomStayCandidate from a JSON string
room_stay_candidate_instance = RoomStayCandidate.from_json(json)
# print the JSON string representation of the object
print RoomStayCandidate.to_json()

# convert the object into a dict
room_stay_candidate_dict = room_stay_candidate_instance.to_dict()
# create an instance of RoomStayCandidate from a dict
room_stay_candidate_form_dict = room_stay_candidate.from_dict(room_stay_candidate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


