# DepositPolicy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**deposit** | [**List[Deposit]**](Deposit.md) |  | 

## Example

```python
from openapi_client.models.deposit_policy import DepositPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of DepositPolicy from a JSON string
deposit_policy_instance = DepositPolicy.from_json(json)
# print the JSON string representation of the object
print DepositPolicy.to_json()

# convert the object into a dict
deposit_policy_dict = deposit_policy_instance.to_dict()
# create an instance of DepositPolicy from a dict
deposit_policy_form_dict = deposit_policy.from_dict(deposit_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


