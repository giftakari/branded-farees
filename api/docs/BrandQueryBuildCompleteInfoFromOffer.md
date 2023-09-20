# BrandQueryBuildCompleteInfoFromOffer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**offer_identifier** | [**OfferIdentifier**](OfferIdentifier.md) |  | 
**product_identifier** | [**List[ProductIdentifier]**](ProductIdentifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.brand_query_build_complete_info_from_offer import BrandQueryBuildCompleteInfoFromOffer

# TODO update the JSON string below
json = "{}"
# create an instance of BrandQueryBuildCompleteInfoFromOffer from a JSON string
brand_query_build_complete_info_from_offer_instance = BrandQueryBuildCompleteInfoFromOffer.from_json(json)
# print the JSON string representation of the object
print BrandQueryBuildCompleteInfoFromOffer.to_json()

# convert the object into a dict
brand_query_build_complete_info_from_offer_dict = brand_query_build_complete_info_from_offer_instance.to_dict()
# create an instance of BrandQueryBuildCompleteInfoFromOffer from a dict
brand_query_build_complete_info_from_offer_form_dict = brand_query_build_complete_info_from_offer.from_dict(brand_query_build_complete_info_from_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


