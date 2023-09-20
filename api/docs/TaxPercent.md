# TaxPercent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | [optional] 
**tax_code** | **str** | Tax code | [optional] 
**reporting_authority** | **str** | Tax reporting authority | [optional] 
**purpose** | **str** | Purpose of tax | [optional] 
**description** | **str** | Description | [optional] 
**included_in_base** | [**YesNoUnknownEnum**](YesNoUnknownEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.tax_percent import TaxPercent

# TODO update the JSON string below
json = "{}"
# create an instance of TaxPercent from a JSON string
tax_percent_instance = TaxPercent.from_json(json)
# print the JSON string representation of the object
print TaxPercent.to_json()

# convert the object into a dict
tax_percent_dict = tax_percent_instance.to_dict()
# create an instance of TaxPercent from a dict
tax_percent_form_dict = tax_percent.from_dict(tax_percent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


