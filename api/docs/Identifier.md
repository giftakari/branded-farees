# Identifier

Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**authority** | **str** | Name of the authoritative system that created this Guid | [optional] 

## Example

```python
from openapi_client.models.identifier import Identifier

# TODO update the JSON string below
json = "{}"
# create an instance of Identifier from a JSON string
identifier_instance = Identifier.from_json(json)
# print the JSON string representation of the object
print Identifier.to_json()

# convert the object into a dict
identifier_dict = identifier_instance.to_dict()
# create an instance of Identifier from a dict
identifier_form_dict = identifier.from_dict(identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


