# CatalogProductOfferings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog_product_offering** | [**List[CatalogProductOffering]**](CatalogProductOffering.md) |  | [optional] 
**upsell_offering** | [**List[UpsellOffering]**](UpsellOffering.md) |  | [optional] 

## Example

```python
from openapi_client.models.catalog_product_offerings import CatalogProductOfferings

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogProductOfferings from a JSON string
catalog_product_offerings_instance = CatalogProductOfferings.from_json(json)
# print the JSON string representation of the object
print CatalogProductOfferings.to_json()

# convert the object into a dict
catalog_product_offerings_dict = catalog_product_offerings_instance.to_dict()
# create an instance of CatalogProductOfferings from a dict
catalog_product_offerings_form_dict = catalog_product_offerings.from_dict(catalog_product_offerings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


