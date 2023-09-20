# BaggageItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**quantity** | **int** | Baggage item quantity | [optional] 
**measurement** | [**List[Measurement]**](Measurement.md) |  | [optional] 
**baggage_fee** | [**CurrencyAmount**](CurrencyAmount.md) |  | [optional] 
**text** | **str** | Text returned from the shop response | [optional] 

## Example

```python
from openapi_client.models.baggage_item import BaggageItem

# TODO update the JSON string below
json = "{}"
# create an instance of BaggageItem from a JSON string
baggage_item_instance = BaggageItem.from_json(json)
# print the JSON string representation of the object
print BaggageItem.to_json()

# convert the object into a dict
baggage_item_dict = baggage_item_instance.to_dict()
# create an instance of BaggageItem from a dict
baggage_item_form_dict = baggage_item.from_dict(baggage_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


