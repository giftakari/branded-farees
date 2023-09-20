# ModifyPriceDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_breakdown** | [**List[PriceBreakdown]**](PriceBreakdown.md) |  | [optional] 

## Example

```python
from openapi_client.models.modify_price_detail import ModifyPriceDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyPriceDetail from a JSON string
modify_price_detail_instance = ModifyPriceDetail.from_json(json)
# print the JSON string representation of the object
print ModifyPriceDetail.to_json()

# convert the object into a dict
modify_price_detail_dict = modify_price_detail_instance.to_dict()
# create an instance of ModifyPriceDetail from a dict
modify_price_detail_form_dict = modify_price_detail.from_dict(modify_price_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


