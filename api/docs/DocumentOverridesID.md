# DocumentOverridesID


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** | The reporting number. | [optional] 
**document_overrides_ref** | **str** |  | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.document_overrides_id import DocumentOverridesID

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentOverridesID from a JSON string
document_overrides_id_instance = DocumentOverridesID.from_json(json)
# print the JSON string representation of the object
print DocumentOverridesID.to_json()

# convert the object into a dict
document_overrides_id_dict = document_overrides_id_instance.to_dict()
# create an instance of DocumentOverridesID from a dict
document_overrides_id_form_dict = document_overrides_id.from_dict(document_overrides_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


