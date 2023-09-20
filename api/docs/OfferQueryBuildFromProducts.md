# OfferQueryBuildFromProducts


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**build_from_products_request** | [**BuildFromProductsRequest**](BuildFromProductsRequest.md) |  | [optional] 
**cabin_preference** | [**CabinPreference**](CabinPreference.md) |  | [optional] 
**payment_criteria** | [**PaymentCriteria**](PaymentCriteria.md) |  | [optional] 
**fare_rule_type** | [**FareRuleEnum**](FareRuleEnum.md) |  | [optional] 
**fare_rule_category** | [**List[FareRuleCategoryEnum]**](FareRuleCategoryEnum.md) |  | [optional] 
**low_fare_finder_ind** | **bool** | If present and true, this is a low fare finder request | [optional] 
**return_branded_fares_ind** | **bool** | If present and true, branded fares are returned | [optional] 
**re_check_inventory_ind** | **bool** | If present and true, then the host system will perform a sell inventory check. | [optional] 
**validate_inventory_ind** | **bool** | If true, the flight inventory will be checked during the price step | [optional] 

## Example

```python
from openapi_client.models.offer_query_build_from_products import OfferQueryBuildFromProducts

# TODO update the JSON string below
json = "{}"
# create an instance of OfferQueryBuildFromProducts from a JSON string
offer_query_build_from_products_instance = OfferQueryBuildFromProducts.from_json(json)
# print the JSON string representation of the object
print OfferQueryBuildFromProducts.to_json()

# convert the object into a dict
offer_query_build_from_products_dict = offer_query_build_from_products_instance.to_dict()
# create an instance of OfferQueryBuildFromProducts from a dict
offer_query_build_from_products_form_dict = offer_query_build_from_products.from_dict(offer_query_build_from_products_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


