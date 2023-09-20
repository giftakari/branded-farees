# TaxBreakdown


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**airport_code** | **str** | The airport location the tax applies to | 
**currency_code** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**amount** | **float** | The amount of the tax applied | [optional] 

## Example

```python
from openapi_client.models.tax_breakdown import TaxBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of TaxBreakdown from a JSON string
tax_breakdown_instance = TaxBreakdown.from_json(json)
# print the JSON string representation of the object
print TaxBreakdown.to_json()

# convert the object into a dict
tax_breakdown_dict = tax_breakdown_instance.to_dict()
# create an instance of TaxBreakdown from a dict
tax_breakdown_form_dict = tax_breakdown.from_dict(tax_breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


