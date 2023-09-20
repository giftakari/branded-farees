# OfferQueryBuildFromCatalogProductOfferings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**payment_criteria** | [**PaymentCriteria**](PaymentCriteria.md) |  | [optional] 
**build_from_catalog_product_offerings_request** | [**BuildFromCatalogProductOfferingsRequest**](BuildFromCatalogProductOfferingsRequest.md) |  | [optional] 

## Example

```python
from openapi_client.models.offer_query_build_from_catalog_product_offerings import OfferQueryBuildFromCatalogProductOfferings

# TODO update the JSON string below
json = "{}"
# create an instance of OfferQueryBuildFromCatalogProductOfferings from a JSON string
offer_query_build_from_catalog_product_offerings_instance = OfferQueryBuildFromCatalogProductOfferings.from_json(json)
# print the JSON string representation of the object
print OfferQueryBuildFromCatalogProductOfferings.to_json()

# convert the object into a dict
offer_query_build_from_catalog_product_offerings_dict = offer_query_build_from_catalog_product_offerings_instance.to_dict()
# create an instance of OfferQueryBuildFromCatalogProductOfferings from a dict
offer_query_build_from_catalog_product_offerings_form_dict = offer_query_build_from_catalog_product_offerings.from_dict(offer_query_build_from_catalog_product_offerings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


