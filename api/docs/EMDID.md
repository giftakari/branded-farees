# EMDID


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | [optional] 
**emd_ref** | **str** |  | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.emdid import EMDID

# TODO update the JSON string below
json = "{}"
# create an instance of EMDID from a JSON string
emdid_instance = EMDID.from_json(json)
# print the JSON string representation of the object
print EMDID.to_json()

# convert the object into a dict
emdid_dict = emdid_instance.to_dict()
# create an instance of EMDID from a dict
emdid_form_dict = emdid.from_dict(emdid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


