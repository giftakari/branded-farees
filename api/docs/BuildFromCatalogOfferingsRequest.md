# BuildFromCatalogOfferingsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**catalog_offerings_identifier** | [**CatalogOfferingsIdentifier**](CatalogOfferingsIdentifier.md) |  | 
**catalog_offering_identifier** | [**CatalogOfferingIdentifier**](CatalogOfferingIdentifier.md) |  | 
**product_identifier** | [**List[ProductIdentifier]**](ProductIdentifier.md) |  | 
**ancillary_offering_identifier** | [**List[AncillaryOfferingIdentifier]**](AncillaryOfferingIdentifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.build_from_catalog_offerings_request import BuildFromCatalogOfferingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BuildFromCatalogOfferingsRequest from a JSON string
build_from_catalog_offerings_request_instance = BuildFromCatalogOfferingsRequest.from_json(json)
# print the JSON string representation of the object
print BuildFromCatalogOfferingsRequest.to_json()

# convert the object into a dict
build_from_catalog_offerings_request_dict = build_from_catalog_offerings_request_instance.to_dict()
# create an instance of BuildFromCatalogOfferingsRequest from a dict
build_from_catalog_offerings_request_form_dict = build_from_catalog_offerings_request.from_dict(build_from_catalog_offerings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


