# PriceBreakdown


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**amount** | [**Amount**](Amount.md) |  | [optional] 
**commission** | [**Commission**](Commission.md) |  | [optional] 

## Example

```python
from openapi_client.models.price_breakdown import PriceBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of PriceBreakdown from a JSON string
price_breakdown_instance = PriceBreakdown.from_json(json)
# print the JSON string representation of the object
print PriceBreakdown.to_json()

# convert the object into a dict
price_breakdown_dict = price_breakdown_instance.to_dict()
# create an instance of PriceBreakdown from a dict
price_breakdown_form_dict = price_breakdown.from_dict(price_breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


