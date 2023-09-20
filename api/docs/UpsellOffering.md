# UpsellOffering


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** | Local indentifier within a given message for this object. | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 
**catalog_product_offering_ref** | **str** | Used to reference another instance of this object in the same message | [optional] 
**sequence** | **int** | NumberDoubleDigit | [optional] 
**departure** | **str** | Departure location | [optional] 
**arrival** | **str** | Arrival location | [optional] 
**brand** | [**List[BrandID]**](BrandID.md) |  | [optional] 
**product_brand_options** | [**List[ProductBrandOptions]**](ProductBrandOptions.md) |  | 
**sponsored_product_brand_options** | [**List[SponsoredProductBrandOptions]**](SponsoredProductBrandOptions.md) |  | [optional] 
**product_refs** | **List[str]** | An unsolicited Offering, offered in conjunction with specified product(s) | [optional] 

## Example

```python
from openapi_client.models.upsell_offering import UpsellOffering

# TODO update the JSON string below
json = "{}"
# create an instance of UpsellOffering from a JSON string
upsell_offering_instance = UpsellOffering.from_json(json)
# print the JSON string representation of the object
print UpsellOffering.to_json()

# convert the object into a dict
upsell_offering_dict = upsell_offering_instance.to_dict()
# create an instance of UpsellOffering from a dict
upsell_offering_form_dict = upsell_offering.from_dict(upsell_offering_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


