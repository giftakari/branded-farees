# PenaltyAmount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**CurrencyAmount**](CurrencyAmount.md) |  | [optional] 

## Example

```python
from openapi_client.models.penalty_amount import PenaltyAmount

# TODO update the JSON string below
json = "{}"
# create an instance of PenaltyAmount from a JSON string
penalty_amount_instance = PenaltyAmount.from_json(json)
# print the JSON string representation of the object
print PenaltyAmount.to_json()

# convert the object into a dict
penalty_amount_dict = penalty_amount_instance.to_dict()
# create an instance of PenaltyAmount from a dict
penalty_amount_form_dict = penalty_amount.from_dict(penalty_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


