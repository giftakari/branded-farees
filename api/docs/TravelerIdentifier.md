# TravelerIdentifier


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**traveler_ref** | **str** |  | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.traveler_identifier import TravelerIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of TravelerIdentifier from a JSON string
traveler_identifier_instance = TravelerIdentifier.from_json(json)
# print the JSON string representation of the object
print TravelerIdentifier.to_json()

# convert the object into a dict
traveler_identifier_dict = traveler_identifier_instance.to_dict()
# create an instance of TravelerIdentifier from a dict
traveler_identifier_form_dict = traveler_identifier.from_dict(traveler_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


