# CabinPreference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**preference_type** | [**CabinPreferenceTypeEnum**](CabinPreferenceTypeEnum.md) |  | [optional] 
**cabins** | [**List[CabinAirEnum]**](CabinAirEnum.md) |  | [optional] 
**leg_sequence** | **List[int]** | Leg sequence | [optional] 

## Example

```python
from openapi_client.models.cabin_preference import CabinPreference

# TODO update the JSON string below
json = "{}"
# create an instance of CabinPreference from a JSON string
cabin_preference_instance = CabinPreference.from_json(json)
# print the JSON string representation of the object
print CabinPreference.to_json()

# convert the object into a dict
cabin_preference_dict = cabin_preference_instance.to_dict()
# create an instance of CabinPreference from a dict
cabin_preference_form_dict = cabin_preference.from_dict(cabin_preference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


