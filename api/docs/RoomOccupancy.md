# RoomOccupancy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**min_occupancy** | **int** | The minimum occupancy | [optional] 
**max_occupancy** | **int** | The maximum number of room occupants. | [optional] 
**age_qualifying** | [**List[AgeQualifying]**](AgeQualifying.md) |  | [optional] 

## Example

```python
from openapi_client.models.room_occupancy import RoomOccupancy

# TODO update the JSON string below
json = "{}"
# create an instance of RoomOccupancy from a JSON string
room_occupancy_instance = RoomOccupancy.from_json(json)
# print the JSON string representation of the object
print RoomOccupancy.to_json()

# convert the object into a dict
room_occupancy_dict = room_occupancy_instance.to_dict()
# create an instance of RoomOccupancy from a dict
room_occupancy_form_dict = room_occupancy.from_dict(room_occupancy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


