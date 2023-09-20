# RoomCharacteristics


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**type_code** | **str** | Type code | [optional] 
**view_code** | **str** | Free text describing the view. | [optional] 
**category** | **str** | Category of the room. | [optional] 
**smoking_allowed** | [**YesNoUnknownEnum**](YesNoUnknownEnum.md) |  | [optional] 
**wifi_included** | [**YesNoUnknownEnum**](YesNoUnknownEnum.md) |  | [optional] 
**bed_configuration** | [**List[BedConfiguration]**](BedConfiguration.md) |  | [optional] 
**non_smoking_ind** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.room_characteristics import RoomCharacteristics

# TODO update the JSON string below
json = "{}"
# create an instance of RoomCharacteristics from a JSON string
room_characteristics_instance = RoomCharacteristics.from_json(json)
# print the JSON string representation of the object
print RoomCharacteristics.to_json()

# convert the object into a dict
room_characteristics_dict = room_characteristics_instance.to_dict()
# create an instance of RoomCharacteristics from a dict
room_characteristics_form_dict = room_characteristics.from_dict(room_characteristics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


