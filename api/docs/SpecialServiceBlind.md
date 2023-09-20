# SpecialServiceBlind


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blind_assistance_requested_ind** | **bool** | If true the Traveler is Blind and requests assistance | [optional] 

## Example

```python
from openapi_client.models.special_service_blind import SpecialServiceBlind

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialServiceBlind from a JSON string
special_service_blind_instance = SpecialServiceBlind.from_json(json)
# print the JSON string representation of the object
print SpecialServiceBlind.to_json()

# convert the object into a dict
special_service_blind_dict = special_service_blind_instance.to_dict()
# create an instance of SpecialServiceBlind from a dict
special_service_blind_form_dict = special_service_blind.from_dict(special_service_blind_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


