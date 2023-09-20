# ProductRateCodeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**product_ref** | **str** | Product reference | [optional] 
**rate_code_info** | [**RateCodeInfo**](RateCodeInfo.md) |  | 

## Example

```python
from openapi_client.models.product_rate_code_info import ProductRateCodeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ProductRateCodeInfo from a JSON string
product_rate_code_info_instance = ProductRateCodeInfo.from_json(json)
# print the JSON string representation of the object
print ProductRateCodeInfo.to_json()

# convert the object into a dict
product_rate_code_info_dict = product_rate_code_info_instance.to_dict()
# create an instance of ProductRateCodeInfo from a dict
product_rate_code_info_form_dict = product_rate_code_info.from_dict(product_rate_code_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


