# ConfirmationHold


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locator** | [**Locator**](Locator.md) |  | 
**offer_status** | [**OfferStatus**](OfferStatus.md) |  | [optional] 
**shopping_cart_product_status** | [**ShoppingCartProductStatusAir**](ShoppingCartProductStatusAir.md) |  | [optional] 

## Example

```python
from openapi_client.models.confirmation_hold import ConfirmationHold

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmationHold from a JSON string
confirmation_hold_instance = ConfirmationHold.from_json(json)
# print the JSON string representation of the object
print ConfirmationHold.to_json()

# convert the object into a dict
confirmation_hold_dict = confirmation_hold_instance.to_dict()
# create an instance of ConfirmationHold from a dict
confirmation_hold_form_dict = confirmation_hold.from_dict(confirmation_hold_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


