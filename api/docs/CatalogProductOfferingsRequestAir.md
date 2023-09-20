# CatalogProductOfferingsRequestAir


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_number_of_offers_to_return** | **int** | This attribute is deprecated and not validated if sent | [optional] 
**offers_per_page** | **int** | Number of offers per page | [optional] 
**content_source_list** | [**List[ContentSourceEnum]**](ContentSourceEnum.md) |  | [optional] 
**max_number_of_upsells_to_return** | **int** | The maximum number of upsells to return | [optional] 
**number_of_downsells_to_return** | **int** | The number of downsells to return | [optional] 
**passenger_criteria** | [**List[PassengerCriteria]**](PassengerCriteria.md) |  | [optional] 
**search_criteria_flight** | [**List[SearchCriteriaFlight]**](SearchCriteriaFlight.md) |  | [optional] 
**search_modifiers_air** | [**SearchModifiersAir**](SearchModifiersAir.md) |  | [optional] 
**payment_criteria** | [**PaymentCriteria**](PaymentCriteria.md) |  | [optional] 
**pricing_modifiers_air** | [**PricingModifiersAir**](PricingModifiersAir.md) |  | [optional] 
**pseudo_city_info** | [**PseudoCityInfo**](PseudoCityInfo.md) |  | [optional] 
**custom_response_modifiers_air** | [**CustomResponseModifiersAir**](CustomResponseModifiersAir.md) |  | [optional] 
**search_type** | [**SearchTypeEnum**](SearchTypeEnum.md) |  | [optional] 
**inhibit_brand_content_ind** | **bool** | if true, brand infromation will be supressed. | [optional] 
**detail_view_ind** | **bool** | if true, detail view should be returned | [optional] 
**exclude_mixed_brands_ind** | **bool** | If true, mixed brands will be inhibited from the response | [optional] 

## Example

```python
from openapi_client.models.catalog_product_offerings_request_air import CatalogProductOfferingsRequestAir

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogProductOfferingsRequestAir from a JSON string
catalog_product_offerings_request_air_instance = CatalogProductOfferingsRequestAir.from_json(json)
# print the JSON string representation of the object
print CatalogProductOfferingsRequestAir.to_json()

# convert the object into a dict
catalog_product_offerings_request_air_dict = catalog_product_offerings_request_air_instance.to_dict()
# create an instance of CatalogProductOfferingsRequestAir from a dict
catalog_product_offerings_request_air_form_dict = catalog_product_offerings_request_air.from_dict(catalog_product_offerings_request_air_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


