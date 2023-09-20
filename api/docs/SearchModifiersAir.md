# SearchModifiersAir


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**exclude_ground** | [**ExcludeGroundTypeEnum**](ExcludeGroundTypeEnum.md) |  | [optional] 
**carrier_preference** | [**List[CarrierPreference]**](CarrierPreference.md) |  | [optional] 
**cabin_preference** | [**List[CabinPreference]**](CabinPreference.md) |  | [optional] 
**class_of_service_preference** | [**List[ClassOfServicePreference]**](ClassOfServicePreference.md) |  | [optional] 
**product_inclusion_preference** | [**List[ProductInclusionPreference]**](ProductInclusionPreference.md) |  | [optional] 
**connection_preferences** | [**List[ConnectionPreferencesAir]**](ConnectionPreferencesAir.md) |  | [optional] 
**prohibit_change_of_airport_ind** | **bool** | If present and true, connections that require a change of airports are not returned | [optional] 

## Example

```python
from openapi_client.models.search_modifiers_air import SearchModifiersAir

# TODO update the JSON string below
json = "{}"
# create an instance of SearchModifiersAir from a JSON string
search_modifiers_air_instance = SearchModifiersAir.from_json(json)
# print the JSON string representation of the object
print SearchModifiersAir.to_json()

# convert the object into a dict
search_modifiers_air_dict = search_modifiers_air_instance.to_dict()
# create an instance of SearchModifiersAir from a dict
search_modifiers_air_form_dict = search_modifiers_air.from_dict(search_modifiers_air_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


