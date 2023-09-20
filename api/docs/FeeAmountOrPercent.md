# FeeAmountOrPercent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**application** | [**CommissionEnum**](CommissionEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.fee_amount_or_percent import FeeAmountOrPercent

# TODO update the JSON string below
json = "{}"
# create an instance of FeeAmountOrPercent from a JSON string
fee_amount_or_percent_instance = FeeAmountOrPercent.from_json(json)
# print the JSON string representation of the object
print FeeAmountOrPercent.to_json()

# convert the object into a dict
fee_amount_or_percent_dict = fee_amount_or_percent_instance.to_dict()
# create an instance of FeeAmountOrPercent from a dict
fee_amount_or_percent_form_dict = fee_amount_or_percent.from_dict(fee_amount_or_percent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


