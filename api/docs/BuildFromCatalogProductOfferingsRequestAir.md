# BuildFromCatalogProductOfferingsRequestAir


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**catalog_product_offerings_identifier** | [**CatalogProductOfferingsIdentifier**](CatalogProductOfferingsIdentifier.md) |  | 
**catalog_product_offering_selection** | [**List[CatalogProductOfferingSelection]**](CatalogProductOfferingSelection.md) |  | 
**upsell_offering_identifier** | [**List[UpsellOfferingIdentifier]**](UpsellOfferingIdentifier.md) |  | [optional] 
**pricing_modifiers_air** | [**PricingModifiersAir**](PricingModifiersAir.md) |  | [optional] 
**cabin_preference** | [**CabinPreference**](CabinPreference.md) |  | [optional] 
**fare_rule_category** | [**List[FareRuleCategoryEnum]**](FareRuleCategoryEnum.md) |  | [optional] 
**fare_rule_type** | [**FareRuleEnum**](FareRuleEnum.md) |  | [optional] 
**custom_response_modifiers_air** | [**CustomResponseModifiersAir**](CustomResponseModifiersAir.md) |  | [optional] 
**low_fare_finder_ind** | **bool** | If true, the price service will return the lowest fare available for the itinerary requested | [optional] 
**re_check_inventory_ind** | **bool** | If true, the price service will recheck inventory at the time of pricing the Offer | [optional] 
**inhibit_brand_content_ind** | **bool** | If true, Brand content will not be returned with the Offer | [optional] 
**validate_inventory_ind** | **bool** | If true, the flight inventory will be checked during the price step | [optional] 

## Example

```python
from openapi_client.models.build_from_catalog_product_offerings_request_air import BuildFromCatalogProductOfferingsRequestAir

# TODO update the JSON string below
json = "{}"
# create an instance of BuildFromCatalogProductOfferingsRequestAir from a JSON string
build_from_catalog_product_offerings_request_air_instance = BuildFromCatalogProductOfferingsRequestAir.from_json(json)
# print the JSON string representation of the object
print BuildFromCatalogProductOfferingsRequestAir.to_json()

# convert the object into a dict
build_from_catalog_product_offerings_request_air_dict = build_from_catalog_product_offerings_request_air_instance.to_dict()
# create an instance of BuildFromCatalogProductOfferingsRequestAir from a dict
build_from_catalog_product_offerings_request_air_form_dict = build_from_catalog_product_offerings_request_air.from_dict(build_from_catalog_product_offerings_request_air_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


