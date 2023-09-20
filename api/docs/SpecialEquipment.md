# SpecialEquipment

A list of special equipment codes from OTA Equipment Type Code

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**equipment_type_code** | **str** |  | [optional] 
**code_context** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.special_equipment import SpecialEquipment

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialEquipment from a JSON string
special_equipment_instance = SpecialEquipment.from_json(json)
# print the JSON string representation of the object
print SpecialEquipment.to_json()

# convert the object into a dict
special_equipment_dict = special_equipment_instance.to_dict()
# create an instance of SpecialEquipment from a dict
special_equipment_form_dict = special_equipment.from_dict(special_equipment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


