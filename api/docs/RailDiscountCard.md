# RailDiscountCard

The name of the Rail Discount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**supplier_code** | **str** | Code of the Supplier | 
**reference_number** | **str** | ReferenceNumber | [optional] 

## Example

```python
from openapi_client.models.rail_discount_card import RailDiscountCard

# TODO update the JSON string below
json = "{}"
# create an instance of RailDiscountCard from a JSON string
rail_discount_card_instance = RailDiscountCard.from_json(json)
# print the JSON string representation of the object
print RailDiscountCard.to_json()

# convert the object into a dict
rail_discount_card_dict = rail_discount_card_instance.to_dict()
# create an instance of RailDiscountCard from a dict
rail_discount_card_form_dict = rail_discount_card.from_dict(rail_discount_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


