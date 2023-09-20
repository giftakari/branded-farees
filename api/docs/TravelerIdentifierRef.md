# TravelerIdentifierRef


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Traveler identifier | [optional] 
**passenger_type_code** | **str** | Passenger Type code | [optional] 
**value** | **str** |  | [optional] 
**id** | **str** | A locally referenced ID | [optional] 
**description** | **str** | Descriptive text used to identify the contents of a target object | [optional] 
**uris** | **List[str]** | Uniform Resource Identifier | [optional] 

## Example

```python
from openapi_client.models.traveler_identifier_ref import TravelerIdentifierRef

# TODO update the JSON string below
json = "{}"
# create an instance of TravelerIdentifierRef from a JSON string
traveler_identifier_ref_instance = TravelerIdentifierRef.from_json(json)
# print the JSON string representation of the object
print TravelerIdentifierRef.to_json()

# convert the object into a dict
traveler_identifier_ref_dict = traveler_identifier_ref_instance.to_dict()
# create an instance of TravelerIdentifierRef from a dict
traveler_identifier_ref_form_dict = traveler_identifier_ref.from_dict(traveler_identifier_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


