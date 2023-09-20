# SignatureOnFile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**date_effective_expire** | [**DateEffectiveExpire**](DateEffectiveExpire.md) |  | [optional] 
**signature_on_file_ind** | **bool** | When true, indicates a signature has been obtained. | [optional] 

## Example

```python
from openapi_client.models.signature_on_file import SignatureOnFile

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureOnFile from a JSON string
signature_on_file_instance = SignatureOnFile.from_json(json)
# print the JSON string representation of the object
print SignatureOnFile.to_json()

# convert the object into a dict
signature_on_file_dict = signature_on_file_instance.to_dict()
# create an instance of SignatureOnFile from a dict
signature_on_file_form_dict = signature_on_file.from_dict(signature_on_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


