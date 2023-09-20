# AmountPercent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**application** | [**CommissionEnum**](CommissionEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.amount_percent import AmountPercent

# TODO update the JSON string below
json = "{}"
# create an instance of AmountPercent from a JSON string
amount_percent_instance = AmountPercent.from_json(json)
# print the JSON string representation of the object
print AmountPercent.to_json()

# convert the object into a dict
amount_percent_dict = amount_percent_instance.to_dict()
# create an instance of AmountPercent from a dict
amount_percent_form_dict = amount_percent.from_dict(amount_percent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


