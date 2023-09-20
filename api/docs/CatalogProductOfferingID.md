# CatalogProductOfferingID


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** | Local indentifier within a given message for this object. | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 
**catalog_product_offering_ref** | **str** | Used to reference another instance of this object in the same message | [optional] 

## Example

```python
from openapi_client.models.catalog_product_offering_id import CatalogProductOfferingID

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogProductOfferingID from a JSON string
catalog_product_offering_id_instance = CatalogProductOfferingID.from_json(json)
# print the JSON string representation of the object
print CatalogProductOfferingID.to_json()

# convert the object into a dict
catalog_product_offering_id_dict = catalog_product_offering_id_instance.to_dict()
# create an instance of CatalogProductOfferingID from a dict
catalog_product_offering_id_form_dict = catalog_product_offering_id.from_dict(catalog_product_offering_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


