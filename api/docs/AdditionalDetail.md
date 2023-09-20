# AdditionalDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**detail_type** | **str** | OTA Code | [optional] 
**code** | **str** | Partner code | [optional] 
**amount** | [**CurrencyAmount**](CurrencyAmount.md) |  | [optional] 
**description** | [**TextTitleAndDescription**](TextTitleAndDescription.md) |  | [optional] 

## Example

```python
from openapi_client.models.additional_detail import AdditionalDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalDetail from a JSON string
additional_detail_instance = AdditionalDetail.from_json(json)
# print the JSON string representation of the object
print AdditionalDetail.to_json()

# convert the object into a dict
additional_detail_dict = additional_detail_instance.to_dict()
# create an instance of AdditionalDetail from a dict
additional_detail_form_dict = additional_detail.from_dict(additional_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


