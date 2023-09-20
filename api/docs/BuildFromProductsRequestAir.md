# BuildFromProductsRequestAir


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pricing_modifiers_air** | [**PricingModifiersAir**](PricingModifiersAir.md) |  | 
**passenger_criteria** | [**List[PassengerCriteria]**](PassengerCriteria.md) |  | 
**product_criteria_air** | [**List[ProductCriteriaAir]**](ProductCriteriaAir.md) |  | 
**custom_response_modifiers_air** | [**List[CustomResponseModifiersAir]**](CustomResponseModifiersAir.md) |  | [optional] 

## Example

```python
from openapi_client.models.build_from_products_request_air import BuildFromProductsRequestAir

# TODO update the JSON string below
json = "{}"
# create an instance of BuildFromProductsRequestAir from a JSON string
build_from_products_request_air_instance = BuildFromProductsRequestAir.from_json(json)
# print the JSON string representation of the object
print BuildFromProductsRequestAir.to_json()

# convert the object into a dict
build_from_products_request_air_dict = build_from_products_request_air_instance.to_dict()
# create an instance of BuildFromProductsRequestAir from a dict
build_from_products_request_air_form_dict = build_from_products_request_air.from_dict(build_from_products_request_air_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


