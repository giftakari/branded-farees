# CatalogProductOfferingIdentifier


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Local indentifier within a given message for this object. | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 
**catalog_product_offering_ref** | **str** | Used to reference another instance of this object in the same message | [optional] 

## Example

```python
from openapi_client.models.catalog_product_offering_identifier import CatalogProductOfferingIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogProductOfferingIdentifier from a JSON string
catalog_product_offering_identifier_instance = CatalogProductOfferingIdentifier.from_json(json)
# print the JSON string representation of the object
print CatalogProductOfferingIdentifier.to_json()

# convert the object into a dict
catalog_product_offering_identifier_dict = catalog_product_offering_identifier_instance.to_dict()
# create an instance of CatalogProductOfferingIdentifier from a dict
catalog_product_offering_identifier_form_dict = catalog_product_offering_identifier.from_dict(catalog_product_offering_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


