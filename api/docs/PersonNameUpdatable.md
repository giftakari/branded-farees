# PersonNameUpdatable


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**prefix** | **str** | Salutation of honorific | 
**given** | **str** | The first given name of the person | 
**middle** | **str** | The middle name of the person | 
**surname** | **str** | Family name, last name | 
**suffix** | **str** | Name suffix | 

## Example

```python
from openapi_client.models.person_name_updatable import PersonNameUpdatable

# TODO update the JSON string below
json = "{}"
# create an instance of PersonNameUpdatable from a JSON string
person_name_updatable_instance = PersonNameUpdatable.from_json(json)
# print the JSON string representation of the object
print PersonNameUpdatable.to_json()

# convert the object into a dict
person_name_updatable_dict = person_name_updatable_instance.to_dict()
# create an instance of PersonNameUpdatable from a dict
person_name_updatable_form_dict = person_name_updatable.from_dict(person_name_updatable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


