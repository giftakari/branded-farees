# PersonNameDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**person_name_type** | [**NameTypeEnum**](NameTypeEnum.md) |  | [optional] 
**language** | **str** | &#39;ISO639 code of the language the name is represented  | [optional] 
**surname_prefix** | **str** | The surname prefix | [optional] 
**suffix** | **str** | Hold various name suffixes and letters | [optional] 
**title** | **str** | Degree or honors | [optional] 
**privacy** | [**Privacy**](Privacy.md) |  | [optional] 
**default_ind** | **bool** | If true, this is the default or primary name within a collection of names. | [optional] 

## Example

```python
from openapi_client.models.person_name_detail import PersonNameDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PersonNameDetail from a JSON string
person_name_detail_instance = PersonNameDetail.from_json(json)
# print the JSON string representation of the object
print PersonNameDetail.to_json()

# convert the object into a dict
person_name_detail_dict = person_name_detail_instance.to_dict()
# create an instance of PersonNameDetail from a dict
person_name_detail_form_dict = person_name_detail.from_dict(person_name_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


