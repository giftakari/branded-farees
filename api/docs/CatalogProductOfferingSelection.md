# CatalogProductOfferingSelection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**catalog_product_offering_identifier** | [**CatalogProductOfferingIdentifier**](CatalogProductOfferingIdentifier.md) |  | 
**product_brand_offering_identifier** | [**Identifier**](Identifier.md) |  | 
**product_identifier** | [**List[ProductIdentifier]**](ProductIdentifier.md) |  | [optional] 
**segment_sequence** | **List[int]** |  | [optional] 

## Example

```python
from openapi_client.models.catalog_product_offering_selection import CatalogProductOfferingSelection

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogProductOfferingSelection from a JSON string
catalog_product_offering_selection_instance = CatalogProductOfferingSelection.from_json(json)
# print the JSON string representation of the object
print CatalogProductOfferingSelection.to_json()

# convert the object into a dict
catalog_product_offering_selection_dict = catalog_product_offering_selection_instance.to_dict()
# create an instance of CatalogProductOfferingSelection from a dict
catalog_product_offering_selection_form_dict = catalog_product_offering_selection.from_dict(catalog_product_offering_selection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


