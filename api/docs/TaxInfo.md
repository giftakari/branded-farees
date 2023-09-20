# TaxInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_code** | **str** | The tax code | 
**currency_code** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**amount** | **float** | The amount of the tax applied | 
**tax_breakdown** | [**List[TaxBreakdown]**](TaxBreakdown.md) | The breakdown of the tax for this tax code | 

## Example

```python
from openapi_client.models.tax_info import TaxInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TaxInfo from a JSON string
tax_info_instance = TaxInfo.from_json(json)
# print the JSON string representation of the object
print TaxInfo.to_json()

# convert the object into a dict
tax_info_dict = tax_info_instance.to_dict()
# create an instance of TaxInfo from a dict
tax_info_form_dict = tax_info.from_dict(tax_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


