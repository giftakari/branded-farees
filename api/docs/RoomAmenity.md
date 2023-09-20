# RoomAmenity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**description** | **str** | description of the room amenity | [optional] 
**quantity** | **int** | quantity of amenity | [optional] 
**name** | **str** | Room Amenity Name | [optional] 
**inclusion** | **List[str]** |  | [optional] 
**included_ind** | **bool** | To represent if the Amenity is included in the rate | [optional] 
**surcharge_ind** | **bool** | To represent if the Amenity attracts a surcharge | [optional] 
**code** | **str** | OTA code used to describe the room amenity. This is optional in the Properties Search request but mandatory in the response | [optional] 

## Example

```python
from openapi_client.models.room_amenity import RoomAmenity

# TODO update the JSON string below
json = "{}"
# create an instance of RoomAmenity from a JSON string
room_amenity_instance = RoomAmenity.from_json(json)
# print the JSON string representation of the object
print RoomAmenity.to_json()

# convert the object into a dict
room_amenity_dict = room_amenity_instance.to_dict()
# create an instance of RoomAmenity from a dict
room_amenity_form_dict = room_amenity.from_dict(room_amenity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


