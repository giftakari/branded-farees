# RefundPenaltyRange


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**minimum** | [**AmountPercent**](AmountPercent.md) |  | [optional] 
**maximum** | [**AmountPercent**](AmountPercent.md) |  | [optional] 

## Example

```python
from openapi_client.models.refund_penalty_range import RefundPenaltyRange

# TODO update the JSON string below
json = "{}"
# create an instance of RefundPenaltyRange from a JSON string
refund_penalty_range_instance = RefundPenaltyRange.from_json(json)
# print the JSON string representation of the object
print RefundPenaltyRange.to_json()

# convert the object into a dict
refund_penalty_range_dict = refund_penalty_range_instance.to_dict()
# create an instance of RefundPenaltyRange from a dict
refund_penalty_range_form_dict = refund_penalty_range.from_dict(refund_penalty_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


