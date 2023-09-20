# PriceDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_breakdown** | [**List[PriceBreakdown]**](PriceBreakdown.md) |  | [optional] 

## Example

```python
from openapi_client.models.price_detail import PriceDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PriceDetail from a JSON string
price_detail_instance = PriceDetail.from_json(json)
# print the JSON string representation of the object
print PriceDetail.to_json()

# convert the object into a dict
price_detail_dict = price_detail_instance.to_dict()
# create an instance of PriceDetail from a dict
price_detail_form_dict = price_detail.from_dict(price_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


