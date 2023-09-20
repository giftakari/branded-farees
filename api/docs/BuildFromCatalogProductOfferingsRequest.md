# BuildFromCatalogProductOfferingsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**catalog_product_offerings_identifier** | [**CatalogProductOfferingsIdentifier**](CatalogProductOfferingsIdentifier.md) |  | 
**catalog_product_offering_selection** | [**List[CatalogProductOfferingSelection]**](CatalogProductOfferingSelection.md) |  | 
**upsell_offering_identifier** | [**List[UpsellOfferingIdentifier]**](UpsellOfferingIdentifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.build_from_catalog_product_offerings_request import BuildFromCatalogProductOfferingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BuildFromCatalogProductOfferingsRequest from a JSON string
build_from_catalog_product_offerings_request_instance = BuildFromCatalogProductOfferingsRequest.from_json(json)
# print the JSON string representation of the object
print BuildFromCatalogProductOfferingsRequest.to_json()

# convert the object into a dict
build_from_catalog_product_offerings_request_dict = build_from_catalog_product_offerings_request_instance.to_dict()
# create an instance of BuildFromCatalogProductOfferingsRequest from a dict
build_from_catalog_product_offerings_request_form_dict = build_from_catalog_product_offerings_request.from_dict(build_from_catalog_product_offerings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


