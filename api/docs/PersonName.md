# PersonName


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**prefix** | **str** | Salutation of honorific (e.g. Mr., Mrs., Ms., Miss, Dr.) | [optional] 
**given** | **str** | Given name, first name or names. | [optional] 
**middle** | **str** | The middle name of the person name. | [optional] 
**surname** | **str** | Family name, last name. | 

## Example

```python
from openapi_client.models.person_name import PersonName

# TODO update the JSON string below
json = "{}"
# create an instance of PersonName from a JSON string
person_name_instance = PersonName.from_json(json)
# print the JSON string representation of the object
print PersonName.to_json()

# convert the object into a dict
person_name_dict = person_name_instance.to_dict()
# create an instance of PersonName from a dict
person_name_form_dict = person_name.from_dict(person_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


