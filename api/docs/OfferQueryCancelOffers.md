# OfferQueryCancelOffers


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [default to 'OfferQueryCancelOffers']
**cancel_offer_request** | [**List[CancelOfferRequest]**](CancelOfferRequest.md) |  | 

## Example

```python
from openapi_client.models.offer_query_cancel_offers import OfferQueryCancelOffers

# TODO update the JSON string below
json = "{}"
# create an instance of OfferQueryCancelOffers from a JSON string
offer_query_cancel_offers_instance = OfferQueryCancelOffers.from_json(json)
# print the JSON string representation of the object
print OfferQueryCancelOffers.to_json()

# convert the object into a dict
offer_query_cancel_offers_dict = offer_query_cancel_offers_instance.to_dict()
# create an instance of OfferQueryCancelOffers from a dict
offer_query_cancel_offers_form_dict = offer_query_cancel_offers.from_dict(offer_query_cancel_offers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


