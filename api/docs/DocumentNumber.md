# DocumentNumber


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**document_issuer** | **str** | Document issuer | [optional] 
**document_type** | [**DocumentTypeEnum**](DocumentTypeEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.document_number import DocumentNumber

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentNumber from a JSON string
document_number_instance = DocumentNumber.from_json(json)
# print the JSON string representation of the object
print DocumentNumber.to_json()

# convert the object into a dict
document_number_dict = document_number_instance.to_dict()
# create an instance of DocumentNumber from a dict
document_number_form_dict = document_number.from_dict(document_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


