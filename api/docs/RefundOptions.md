# RefundOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**refund_types** | [**List[RefundTypeEnum]**](RefundTypeEnum.md) |  | 
**refund_penalty_range** | [**RefundPenaltyRange**](RefundPenaltyRange.md) |  | [optional] 

## Example

```python
from openapi_client.models.refund_options import RefundOptions

# TODO update the JSON string below
json = "{}"
# create an instance of RefundOptions from a JSON string
refund_options_instance = RefundOptions.from_json(json)
# print the JSON string representation of the object
print RefundOptions.to_json()

# convert the object into a dict
refund_options_dict = refund_options_instance.to_dict()
# create an instance of RefundOptions from a dict
refund_options_form_dict = refund_options.from_dict(refund_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


