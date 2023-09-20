# AppliesToOfferProduct


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_identifier** | [**OfferIdentifier**](OfferIdentifier.md) |  | [optional] 
**product_identifier** | [**List[ProductIdentifier]**](ProductIdentifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.applies_to_offer_product import AppliesToOfferProduct

# TODO update the JSON string below
json = "{}"
# create an instance of AppliesToOfferProduct from a JSON string
applies_to_offer_product_instance = AppliesToOfferProduct.from_json(json)
# print the JSON string representation of the object
print AppliesToOfferProduct.to_json()

# convert the object into a dict
applies_to_offer_product_dict = applies_to_offer_product_instance.to_dict()
# create an instance of AppliesToOfferProduct from a dict
applies_to_offer_product_form_dict = applies_to_offer_product.from_dict(applies_to_offer_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


