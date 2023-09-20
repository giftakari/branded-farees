# ClassOfServicePreference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**leg_sequence** | **List[int]** | The legSequence value | [optional] 
**classes_of_service** | **List[str]** | Allows user to specify which class(s) of service they want returned in CatalogOfferings | 
**preference_type** | [**ClassOfServicePreferenceTypeEnum**](ClassOfServicePreferenceTypeEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.class_of_service_preference import ClassOfServicePreference

# TODO update the JSON string below
json = "{}"
# create an instance of ClassOfServicePreference from a JSON string
class_of_service_preference_instance = ClassOfServicePreference.from_json(json)
# print the JSON string representation of the object
print ClassOfServicePreference.to_json()

# convert the object into a dict
class_of_service_preference_dict = class_of_service_preference_instance.to_dict()
# create an instance of ClassOfServicePreference from a dict
class_of_service_preference_form_dict = class_of_service_preference.from_dict(class_of_service_preference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


