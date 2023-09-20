# CommissionAmount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**CurrencyAmount**](CurrencyAmount.md) |  | [optional] 

## Example

```python
from openapi_client.models.commission_amount import CommissionAmount

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionAmount from a JSON string
commission_amount_instance = CommissionAmount.from_json(json)
# print the JSON string representation of the object
print CommissionAmount.to_json()

# convert the object into a dict
commission_amount_dict = commission_amount_instance.to_dict()
# create an instance of CommissionAmount from a dict
commission_amount_form_dict = commission_amount.from_dict(commission_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


