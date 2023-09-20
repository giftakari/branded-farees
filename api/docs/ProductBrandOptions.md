# ProductBrandOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**flight_refs** | **List[str]** | Reference to the Flights that are used within ProductBrandOptions | [optional] 
**product_brand_offering** | [**List[ProductBrandOffering]**](ProductBrandOffering.md) |  | 

## Example

```python
from openapi_client.models.product_brand_options import ProductBrandOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ProductBrandOptions from a JSON string
product_brand_options_instance = ProductBrandOptions.from_json(json)
# print the JSON string representation of the object
print ProductBrandOptions.to_json()

# convert the object into a dict
product_brand_options_dict = product_brand_options_instance.to_dict()
# create an instance of ProductBrandOptions from a dict
product_brand_options_form_dict = product_brand_options.from_dict(product_brand_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


