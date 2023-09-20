# TaxExemption


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**countries** | **List[str]** | ISO country code | [optional] 
**tax_codes** | **List[str]** | Tax codes | [optional] 
**all_taxes_exempt_ind** | **bool** | If true, the Offer/Offering is exempt from all taxes | [optional] 

## Example

```python
from openapi_client.models.tax_exemption import TaxExemption

# TODO update the JSON string below
json = "{}"
# create an instance of TaxExemption from a JSON string
tax_exemption_instance = TaxExemption.from_json(json)
# print the JSON string representation of the object
print TaxExemption.to_json()

# convert the object into a dict
tax_exemption_dict = tax_exemption_instance.to_dict()
# create an instance of TaxExemption from a dict
tax_exemption_form_dict = tax_exemption.from_dict(tax_exemption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


