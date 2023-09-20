# EMDDescription

A description of the ancillary with two description codes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**code** | **str** | A description of the ancillary with two description codes | [optional] 
**sub_code** | **str** | EMD number sub code | [optional] 
**code_context** | **str** | Code context | [optional] 

## Example

```python
from openapi_client.models.emd_description import EMDDescription

# TODO update the JSON string below
json = "{}"
# create an instance of EMDDescription from a JSON string
emd_description_instance = EMDDescription.from_json(json)
# print the JSON string representation of the object
print EMDDescription.to_json()

# convert the object into a dict
emd_description_dict = emd_description_instance.to_dict()
# create an instance of EMDDescription from a dict
emd_description_form_dict = emd_description.from_dict(emd_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


