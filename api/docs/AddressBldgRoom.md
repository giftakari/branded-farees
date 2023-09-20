# AddressBldgRoom

Address with building and room number

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**bulding_ind** | **bool** | When true, the information is a building name. When false, it is an apartment or room # | [optional] 

## Example

```python
from openapi_client.models.address_bldg_room import AddressBldgRoom

# TODO update the JSON string below
json = "{}"
# create an instance of AddressBldgRoom from a JSON string
address_bldg_room_instance = AddressBldgRoom.from_json(json)
# print the JSON string representation of the object
print AddressBldgRoom.to_json()

# convert the object into a dict
address_bldg_room_dict = address_bldg_room_instance.to_dict()
# create an instance of AddressBldgRoom from a dict
address_bldg_room_form_dict = address_bldg_room.from_dict(address_bldg_room_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


