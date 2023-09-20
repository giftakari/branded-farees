# Discount

Corporate or Other discount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | [optional] 
**description** | **str** | The marketing description for the discount | [optional] 
**currency_code** | **str** | Currency code of the city. | 
**code_authority** | **str** | Code Authority | 
**decimal_place** | **int** | Number of decimal places | 
**decimal_authority** | **str** | Decimal Authority | [optional] 

## Example

```python
from openapi_client.models.discount import Discount

# TODO update the JSON string below
json = "{}"
# create an instance of Discount from a JSON string
discount_instance = Discount.from_json(json)
# print the JSON string representation of the object
print Discount.to_json()

# convert the object into a dict
discount_dict = discount_instance.to_dict()
# create an instance of Discount from a dict
discount_form_dict = discount.from_dict(discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


