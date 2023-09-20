# Fee


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**fee_code** | **str** | Fee code | [optional] 
**reporting_authority** | **str** | Identifies the reporting authority. | [optional] 
**purpose** | **str** | Fee purpose | [optional] 
**description** | **str** | Fee description | [optional] 
**fee_application** | [**ApplicationEnum**](ApplicationEnum.md) |  | [optional] 
**fee_frequency** | [**FrequencyEnum**](FrequencyEnum.md) |  | [optional] 
**fee_amount_or_percent** | [**FeeAmountOrPercent**](FeeAmountOrPercent.md) |  | 
**tax** | [**List[Tax]**](Tax.md) |  | [optional] 
**includedin_base_ind** | **bool** | If the fee is included in the Base Price | [optional] 

## Example

```python
from openapi_client.models.fee import Fee

# TODO update the JSON string below
json = "{}"
# create an instance of Fee from a JSON string
fee_instance = Fee.from_json(json)
# print the JSON string representation of the object
print Fee.to_json()

# convert the object into a dict
fee_dict = fee_instance.to_dict()
# create an instance of Fee from a dict
fee_form_dict = fee.from_dict(fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


