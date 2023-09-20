# CatalogProductOfferingsQueryRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**catalog_product_offerings_request** | [**CatalogProductOfferingsRequestAir**](CatalogProductOfferingsRequestAir.md) |  | 

## Example

```python
from openapi_client.models.catalog_product_offerings_query_request import CatalogProductOfferingsQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogProductOfferingsQueryRequest from a JSON string
catalog_product_offerings_query_request_instance = CatalogProductOfferingsQueryRequest.from_json(json)
# print the JSON string representation of the object
print CatalogProductOfferingsQueryRequest.to_json()

# convert the object into a dict
catalog_product_offerings_query_request_dict = catalog_product_offerings_query_request_instance.to_dict()
# create an instance of CatalogProductOfferingsQueryRequest from a dict
catalog_product_offerings_query_request_form_dict = catalog_product_offerings_query_request.from_dict(catalog_product_offerings_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


