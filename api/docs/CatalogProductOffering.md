# CatalogProductOffering


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sequence** | **int** | NumberDoubleDigit | [optional] 
**departure** | **str** | Departure location | [optional] 
**arrival** | **str** | Arrival location | [optional] 
**brand** | [**List[BrandID]**](BrandID.md) |  | [optional] 
**product_brand_options** | [**List[ProductBrandOptions]**](ProductBrandOptions.md) |  | 
**sponsored_product_brand_options** | [**List[SponsoredProductBrandOptions]**](SponsoredProductBrandOptions.md) |  | [optional] 

## Example

```python
from openapi_client.models.catalog_product_offering import CatalogProductOffering

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogProductOffering from a JSON string
catalog_product_offering_instance = CatalogProductOffering.from_json(json)
# print the JSON string representation of the object
print CatalogProductOffering.to_json()

# convert the object into a dict
catalog_product_offering_dict = catalog_product_offering_instance.to_dict()
# create an instance of CatalogProductOffering from a dict
catalog_product_offering_form_dict = catalog_product_offering.from_dict(catalog_product_offering_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


