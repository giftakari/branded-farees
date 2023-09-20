# ConnectionPreferences


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**leg_sequence** | **List[int]** | Leg sequence | [optional] 
**max_connection_duration** | **str** | The maximum acceptable duration of the connection ISO8601 | [optional] 
**max_overnight_duration** | **str** | The maximum acceptable overnight duration of the connection ISO8601 | [optional] 
**preference_type** | [**ConnectionPointPreferenceTypeENUM**](ConnectionPointPreferenceTypeENUM.md) |  | [optional] 
**connection_point** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.connection_preferences import ConnectionPreferences

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionPreferences from a JSON string
connection_preferences_instance = ConnectionPreferences.from_json(json)
# print the JSON string representation of the object
print ConnectionPreferences.to_json()

# convert the object into a dict
connection_preferences_dict = connection_preferences_instance.to_dict()
# create an instance of ConnectionPreferences from a dict
connection_preferences_form_dict = connection_preferences.from_dict(connection_preferences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


