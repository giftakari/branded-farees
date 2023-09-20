# Preference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applies_to** | [**AppliesTo**](AppliesTo.md) |  | [optional] 
**traveler_identifier** | [**TravelerIdentifier**](TravelerIdentifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.preference import Preference

# TODO update the JSON string below
json = "{}"
# create an instance of Preference from a JSON string
preference_instance = Preference.from_json(json)
# print the JSON string representation of the object
print Preference.to_json()

# convert the object into a dict
preference_dict = preference_instance.to_dict()
# create an instance of Preference from a dict
preference_form_dict = preference.from_dict(preference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


