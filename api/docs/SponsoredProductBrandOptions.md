# SponsoredProductBrandOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**flight_refs** | **List[str]** | Reference to the Flights that are used within  SponsoredProductBrandOptions | [optional] 
**product_brand_offering** | [**List[ProductBrandOffering]**](ProductBrandOffering.md) |  | 

## Example

```python
from openapi_client.models.sponsored_product_brand_options import SponsoredProductBrandOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SponsoredProductBrandOptions from a JSON string
sponsored_product_brand_options_instance = SponsoredProductBrandOptions.from_json(json)
# print the JSON string representation of the object
print SponsoredProductBrandOptions.to_json()

# convert the object into a dict
sponsored_product_brand_options_dict = sponsored_product_brand_options_instance.to_dict()
# create an instance of SponsoredProductBrandOptions from a dict
sponsored_product_brand_options_form_dict = sponsored_product_brand_options.from_dict(sponsored_product_brand_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


