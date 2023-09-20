# Deposit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**var_date** | **datetime** | The date and time the deposit is due | [optional] 
**remainder_ind** | **bool** | If present and true, the date is when the remainder of the deposit is due | [optional] 

## Example

```python
from openapi_client.models.deposit import Deposit

# TODO update the JSON string below
json = "{}"
# create an instance of Deposit from a JSON string
deposit_instance = Deposit.from_json(json)
# print the JSON string representation of the object
print Deposit.to_json()

# convert the object into a dict
deposit_dict = deposit_instance.to_dict()
# create an instance of Deposit from a dict
deposit_form_dict = deposit.from_dict(deposit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


