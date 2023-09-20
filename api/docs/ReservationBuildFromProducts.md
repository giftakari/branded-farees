# ReservationBuildFromProducts


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_criteria_air** | [**List[ProductCriteriaAir]**](ProductCriteriaAir.md) |  | 
**pricing_modifiers_air** | [**PricingModifiersAir**](PricingModifiersAir.md) |  | [optional] 

## Example

```python
from openapi_client.models.reservation_build_from_products import ReservationBuildFromProducts

# TODO update the JSON string below
json = "{}"
# create an instance of ReservationBuildFromProducts from a JSON string
reservation_build_from_products_instance = ReservationBuildFromProducts.from_json(json)
# print the JSON string representation of the object
print ReservationBuildFromProducts.to_json()

# convert the object into a dict
reservation_build_from_products_dict = reservation_build_from_products_instance.to_dict()
# create an instance of ReservationBuildFromProducts from a dict
reservation_build_from_products_form_dict = reservation_build_from_products.from_dict(reservation_build_from_products_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


