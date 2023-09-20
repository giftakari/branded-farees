# ProductQueryBuildFromProducts


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_criteria_air** | [**List[ProductCriteriaAir]**](ProductCriteriaAir.md) |  | 
**passenger_criteria** | [**List[PassengerCriteria]**](PassengerCriteria.md) |  | 

## Example

```python
from openapi_client.models.product_query_build_from_products import ProductQueryBuildFromProducts

# TODO update the JSON string below
json = "{}"
# create an instance of ProductQueryBuildFromProducts from a JSON string
product_query_build_from_products_instance = ProductQueryBuildFromProducts.from_json(json)
# print the JSON string representation of the object
print ProductQueryBuildFromProducts.to_json()

# convert the object into a dict
product_query_build_from_products_dict = product_query_build_from_products_instance.to_dict()
# create an instance of ProductQueryBuildFromProducts from a dict
product_query_build_from_products_form_dict = product_query_build_from_products.from_dict(product_query_build_from_products_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


