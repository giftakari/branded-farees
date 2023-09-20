# AncillaryOfferingIdentifier


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Local indentifier within a given message for this object. | [optional] 
**catalog_offering_ref** | **str** | Used to reference another instance of this object in the same message | [optional] 
**ancillary_offering_ref** | **str** |  | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.ancillary_offering_identifier import AncillaryOfferingIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of AncillaryOfferingIdentifier from a JSON string
ancillary_offering_identifier_instance = AncillaryOfferingIdentifier.from_json(json)
# print the JSON string representation of the object
print AncillaryOfferingIdentifier.to_json()

# convert the object into a dict
ancillary_offering_identifier_dict = ancillary_offering_identifier_instance.to_dict()
# create an instance of AncillaryOfferingIdentifier from a dict
ancillary_offering_identifier_form_dict = ancillary_offering_identifier.from_dict(ancillary_offering_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


