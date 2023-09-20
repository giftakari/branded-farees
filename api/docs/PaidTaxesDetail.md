# PaidTaxesDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax** | [**List[Tax]**](Tax.md) |  | [optional] 
**tax_percent** | [**TaxPercent**](TaxPercent.md) |  | [optional] 

## Example

```python
from openapi_client.models.paid_taxes_detail import PaidTaxesDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PaidTaxesDetail from a JSON string
paid_taxes_detail_instance = PaidTaxesDetail.from_json(json)
# print the JSON string representation of the object
print PaidTaxesDetail.to_json()

# convert the object into a dict
paid_taxes_detail_dict = paid_taxes_detail_instance.to_dict()
# create an instance of PaidTaxesDetail from a dict
paid_taxes_detail_form_dict = paid_taxes_detail.from_dict(paid_taxes_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


