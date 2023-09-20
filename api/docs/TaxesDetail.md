# TaxesDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax** | [**List[Tax]**](Tax.md) |  | [optional] 
**tax_percent** | [**TaxPercent**](TaxPercent.md) |  | [optional] 

## Example

```python
from openapi_client.models.taxes_detail import TaxesDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TaxesDetail from a JSON string
taxes_detail_instance = TaxesDetail.from_json(json)
# print the JSON string representation of the object
print TaxesDetail.to_json()

# convert the object into a dict
taxes_detail_dict = taxes_detail_instance.to_dict()
# create an instance of TaxesDetail from a dict
taxes_detail_form_dict = taxes_detail.from_dict(taxes_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


