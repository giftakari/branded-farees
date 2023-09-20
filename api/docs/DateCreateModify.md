# DateCreateModify

Time stamp of the creation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **datetime** |  | [optional] 
**creator_id** | **str** | ID of creator. Software system identifier or an employee id | [optional] 
**last_modify** | **datetime** | Time stamp of last modification. | [optional] 
**last_modifier_id** | **str** | Identifies the last software system or person to modify a record | [optional] 
**purge** | **date** | Date an item will be purged from a system of record | [optional] 

## Example

```python
from openapi_client.models.date_create_modify import DateCreateModify

# TODO update the JSON string below
json = "{}"
# create an instance of DateCreateModify from a JSON string
date_create_modify_instance = DateCreateModify.from_json(json)
# print the JSON string representation of the object
print DateCreateModify.to_json()

# convert the object into a dict
date_create_modify_dict = date_create_modify_instance.to_dict()
# create an instance of DateCreateModify from a dict
date_create_modify_form_dict = date_create_modify.from_dict(date_create_modify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


