# CatalogOfferingIdentifier


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Local indentifier within a given message for this object. | [optional] 
**catalog_offering_ref** | **str** | Used to reference another instance of this object in the same message | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.catalog_offering_identifier import CatalogOfferingIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogOfferingIdentifier from a JSON string
catalog_offering_identifier_instance = CatalogOfferingIdentifier.from_json(json)
# print the JSON string representation of the object
print CatalogOfferingIdentifier.to_json()

# convert the object into a dict
catalog_offering_identifier_dict = catalog_offering_identifier_instance.to_dict()
# create an instance of CatalogOfferingIdentifier from a dict
catalog_offering_identifier_form_dict = catalog_offering_identifier.from_dict(catalog_offering_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


