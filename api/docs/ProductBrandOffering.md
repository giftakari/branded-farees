# ProductBrandOffering


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 
**price** | [**PriceDetail**](PriceDetail.md) |  | [optional] 
**brand** | [**BrandID**](BrandID.md) |  | [optional] 
**product** | [**List[ProductID]**](ProductID.md) |  | [optional] 
**terms_and_conditions** | [**TermsAndConditionsID**](TermsAndConditionsID.md) |  | [optional] 
**combinability_code** | **List[str]** |  | [optional] 
**best_combinable_price** | [**BestCombinablePriceDetail**](BestCombinablePriceDetail.md) |  | [optional] 
**desirability** | **float** | The desirability of the offering expressed as a percentage. The higher the percentage the more desirable the offering. | [optional] 
**matched_attributes** | **int** | The number of matched attributes according to the request modifiers | [optional] 
**brand_status** | [**BrandStatusEnum**](BrandStatusEnum.md) |  | [optional] 
**best_match_ind** | **bool** | If true, this Offering is the best match according to the request modifiers | [optional] 
**co2_emissions_data** | [**CO2EmissionsData**](CO2EmissionsData.md) |  | [optional] 

## Example

```python
from openapi_client.models.product_brand_offering import ProductBrandOffering

# TODO update the JSON string below
json = "{}"
# create an instance of ProductBrandOffering from a JSON string
product_brand_offering_instance = ProductBrandOffering.from_json(json)
# print the JSON string representation of the object
print ProductBrandOffering.to_json()

# convert the object into a dict
product_brand_offering_dict = product_brand_offering_instance.to_dict()
# create an instance of ProductBrandOffering from a dict
product_brand_offering_form_dict = product_brand_offering.from_dict(product_brand_offering_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


