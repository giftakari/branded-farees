# RateCodeInfo

Rate Code

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**rate_name** | **str** | Rate code name | [optional] 
**rate_id** | **str** | Identifier for the rate code | [optional] 
**rate_category** | [**RateCategoryEnum**](RateCategoryEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.rate_code_info import RateCodeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RateCodeInfo from a JSON string
rate_code_info_instance = RateCodeInfo.from_json(json)
# print the JSON string representation of the object
print RateCodeInfo.to_json()

# convert the object into a dict
rate_code_info_dict = rate_code_info_instance.to_dict()
# create an instance of RateCodeInfo from a dict
rate_code_info_form_dict = rate_code_info.from_dict(rate_code_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


