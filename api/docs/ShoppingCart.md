# ShoppingCart


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**product** | [**List[ProductAir]**](ProductAir.md) |  | [optional] 

## Example

```python
from openapi_client.models.shopping_cart import ShoppingCart

# TODO update the JSON string below
json = "{}"
# create an instance of ShoppingCart from a JSON string
shopping_cart_instance = ShoppingCart.from_json(json)
# print the JSON string representation of the object
print ShoppingCart.to_json()

# convert the object into a dict
shopping_cart_dict = shopping_cart_instance.to_dict()
# create an instance of ShoppingCart from a dict
shopping_cart_form_dict = shopping_cart.from_dict(shopping_cart_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


