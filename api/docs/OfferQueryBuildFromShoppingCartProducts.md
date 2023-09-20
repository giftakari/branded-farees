# OfferQueryBuildFromShoppingCartProducts


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**pricing_modifiers_air** | [**PricingModifiersAir**](PricingModifiersAir.md) |  | [optional] 
**product_identifier** | [**List[ProductID]**](ProductID.md) |  | [optional] 
**payment_criteria** | [**PaymentCriteria**](PaymentCriteria.md) |  | [optional] 

## Example

```python
from openapi_client.models.offer_query_build_from_shopping_cart_products import OfferQueryBuildFromShoppingCartProducts

# TODO update the JSON string below
json = "{}"
# create an instance of OfferQueryBuildFromShoppingCartProducts from a JSON string
offer_query_build_from_shopping_cart_products_instance = OfferQueryBuildFromShoppingCartProducts.from_json(json)
# print the JSON string representation of the object
print OfferQueryBuildFromShoppingCartProducts.to_json()

# convert the object into a dict
offer_query_build_from_shopping_cart_products_dict = offer_query_build_from_shopping_cart_products_instance.to_dict()
# create an instance of OfferQueryBuildFromShoppingCartProducts from a dict
offer_query_build_from_shopping_cart_products_form_dict = offer_query_build_from_shopping_cart_products.from_dict(offer_query_build_from_shopping_cart_products_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


