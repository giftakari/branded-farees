# TravelerProduct


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**traveler_ref** | **str** | A pointer to the traveler id | [optional] 
**offer_ref** | **str** | A pointer to the Offer id | [optional] 
**product_ref** | **str** | A pointer to the product id | [optional] 
**confirmation_status_enum** | [**ConfirmationStatusEnum**](ConfirmationStatusEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.traveler_product import TravelerProduct

# TODO update the JSON string below
json = "{}"
# create an instance of TravelerProduct from a JSON string
traveler_product_instance = TravelerProduct.from_json(json)
# print the JSON string representation of the object
print TravelerProduct.to_json()

# convert the object into a dict
traveler_product_dict = traveler_product_instance.to_dict()
# create an instance of TravelerProduct from a dict
traveler_product_form_dict = traveler_product.from_dict(traveler_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


