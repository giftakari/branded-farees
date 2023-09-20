# OfferQueryBuildFromOffer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**build_from_offer** | [**BuildFromOffer**](BuildFromOffer.md) |  | 
**price_historical_offer_ind** | **bool** | If true, the new Offer should be priced using the original Offer create date. | [optional] 
**price_historical_tax_ind** | **bool** | if true, the taxes in the new Offer should be priced using the original Offer create date. | [optional] 
**price_historical_fee_ind** | **bool** | if true, the fees in the new Offer should be priced using the original Offer create date. | [optional] 

## Example

```python
from openapi_client.models.offer_query_build_from_offer import OfferQueryBuildFromOffer

# TODO update the JSON string below
json = "{}"
# create an instance of OfferQueryBuildFromOffer from a JSON string
offer_query_build_from_offer_instance = OfferQueryBuildFromOffer.from_json(json)
# print the JSON string representation of the object
print OfferQueryBuildFromOffer.to_json()

# convert the object into a dict
offer_query_build_from_offer_dict = offer_query_build_from_offer_instance.to_dict()
# create an instance of OfferQueryBuildFromOffer from a dict
offer_query_build_from_offer_form_dict = offer_query_build_from_offer.from_dict(offer_query_build_from_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


