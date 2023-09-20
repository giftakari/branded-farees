# RoomType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**room_characteristics** | [**RoomCharacteristics**](RoomCharacteristics.md) |  | [optional] 
**description** | [**TextTitleAndDescription**](TextTitleAndDescription.md) |  | [optional] 
**room_amenity** | [**List[RoomAmenity]**](RoomAmenity.md) |  | [optional] 

## Example

```python
from openapi_client.models.room_type import RoomType

# TODO update the JSON string below
json = "{}"
# create an instance of RoomType from a JSON string
room_type_instance = RoomType.from_json(json)
# print the JSON string representation of the object
print RoomType.to_json()

# convert the object into a dict
room_type_dict = room_type_instance.to_dict()
# create an instance of RoomType from a dict
room_type_form_dict = room_type.from_dict(room_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


