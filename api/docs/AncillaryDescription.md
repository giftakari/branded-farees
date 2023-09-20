# AncillaryDescription

A description of the ancillary with two description codes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**code** | **str** | The code value | [optional] 
**sub_code** | **str** | The subcode value | [optional] 
**code_context** | **str** | The code Context value | [optional] 

## Example

```python
from openapi_client.models.ancillary_description import AncillaryDescription

# TODO update the JSON string below
json = "{}"
# create an instance of AncillaryDescription from a JSON string
ancillary_description_instance = AncillaryDescription.from_json(json)
# print the JSON string representation of the object
print AncillaryDescription.to_json()

# convert the object into a dict
ancillary_description_dict = ancillary_description_instance.to_dict()
# create an instance of AncillaryDescription from a dict
ancillary_description_form_dict = ancillary_description.from_dict(ancillary_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


