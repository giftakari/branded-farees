# PaidTaxes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**total_taxes** | **float** | A monetary amount, up to 4 decimal places. Decimal place needs to be included. | [optional] 

## Example

```python
from openapi_client.models.paid_taxes import PaidTaxes

# TODO update the JSON string below
json = "{}"
# create an instance of PaidTaxes from a JSON string
paid_taxes_instance = PaidTaxes.from_json(json)
# print the JSON string representation of the object
print PaidTaxes.to_json()

# convert the object into a dict
paid_taxes_dict = paid_taxes_instance.to_dict()
# create an instance of PaidTaxes from a dict
paid_taxes_form_dict = paid_taxes.from_dict(paid_taxes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


