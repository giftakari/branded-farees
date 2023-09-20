# CarrierPreference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**preference_type** | [**CarrierPreferenceTypeEnum**](CarrierPreferenceTypeEnum.md) |  | 
**carriers** | **List[str]** | Carrier airline codes | 
**leg_sequence** | **List[int]** | Leg sequence | [optional] 

## Example

```python
from openapi_client.models.carrier_preference import CarrierPreference

# TODO update the JSON string below
json = "{}"
# create an instance of CarrierPreference from a JSON string
carrier_preference_instance = CarrierPreference.from_json(json)
# print the JSON string representation of the object
print CarrierPreference.to_json()

# convert the object into a dict
carrier_preference_dict = carrier_preference_instance.to_dict()
# create an instance of CarrierPreference from a dict
carrier_preference_form_dict = carrier_preference.from_dict(carrier_preference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


