# RoomTypeDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_units** | **int** | The number of rooms that have been combined to create this room type. | [optional] 
**reqd_guarantee_type** | **str** | TODO-(Should this be Guarantee?)Denotes the form of guarantee for this room. | [optional] 
**additional_details** | [**AdditionalDetails**](AdditionalDetails.md) |  | [optional] 
**room_occupancy** | [**List[RoomOccupancy]**](RoomOccupancy.md) |  | [optional] 
**room_ind** | **bool** | Indicates the room is a sleeping room when true. | [optional] 
**converted_ind** | **bool** | Indicates the room is converted when true. | [optional] 
**alternate_ind** | **bool** | Indicates the room is an alternate room type to the requested room type when true. | [optional] 

## Example

```python
from openapi_client.models.room_type_detail import RoomTypeDetail

# TODO update the JSON string below
json = "{}"
# create an instance of RoomTypeDetail from a JSON string
room_type_detail_instance = RoomTypeDetail.from_json(json)
# print the JSON string representation of the object
print RoomTypeDetail.to_json()

# convert the object into a dict
room_type_detail_dict = room_type_detail_instance.to_dict()
# create an instance of RoomTypeDetail from a dict
room_type_detail_form_dict = room_type_detail.from_dict(room_type_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


