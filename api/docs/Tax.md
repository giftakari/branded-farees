# Tax


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | [optional] 
**currency_code** | **str** | Currency code of the city. | [optional] 
**tax_code** | **str** | Tax code of the city | [optional] 
**reporting_authority** | **str** | Identifies the reporting authority such as airport code for XF taxes. | [optional] 
**purpose** | **str** | purpose | [optional] 
**description** | **str** | additional information | [optional] 
**included_in_base** | [**YesNoUnknownEnum**](YesNoUnknownEnum.md) |  | [optional] 
**code_authority** | **str** | Code Authority | [optional] 
**decimal_place** | **int** | Allowed number of decimals. | [optional] 
**decimal_authority** | **str** | Decimal Authority | [optional] 
**exempt_ind** | **bool** | If true, this tax is exempt | [optional] 

## Example

```python
from openapi_client.models.tax import Tax

# TODO update the JSON string below
json = "{}"
# create an instance of Tax from a JSON string
tax_instance = Tax.from_json(json)
# print the JSON string representation of the object
print Tax.to_json()

# convert the object into a dict
tax_dict = tax_instance.to_dict()
# create an instance of Tax from a dict
tax_form_dict = tax.from_dict(tax_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


