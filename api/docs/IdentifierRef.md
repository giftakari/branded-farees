# IdentifierRef


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**id** | **str** | A locally referenced ID | [optional] 
**description** | **str** | Descriptive text used to identify the contents of a target object | [optional] 
**uris** | **List[str]** | Uniform Resource Identifier | [optional] 

## Example

```python
from openapi_client.models.identifier_ref import IdentifierRef

# TODO update the JSON string below
json = "{}"
# create an instance of IdentifierRef from a JSON string
identifier_ref_instance = IdentifierRef.from_json(json)
# print the JSON string representation of the object
print IdentifierRef.to_json()

# convert the object into a dict
identifier_ref_dict = identifier_ref_instance.to_dict()
# create an instance of IdentifierRef from a dict
identifier_ref_form_dict = identifier_ref.from_dict(identifier_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


