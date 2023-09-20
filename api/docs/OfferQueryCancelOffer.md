# OfferQueryCancelOffer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**build_from_offer** | [**BuildFromOffer**](BuildFromOffer.md) |  | 
**traveler_identifier** | [**List[TravelerIdentifierRef]**](TravelerIdentifierRef.md) |  | [optional] 

## Example

```python
from openapi_client.models.offer_query_cancel_offer import OfferQueryCancelOffer

# TODO update the JSON string below
json = "{}"
# create an instance of OfferQueryCancelOffer from a JSON string
offer_query_cancel_offer_instance = OfferQueryCancelOffer.from_json(json)
# print the JSON string representation of the object
print OfferQueryCancelOffer.to_json()

# convert the object into a dict
offer_query_cancel_offer_dict = offer_query_cancel_offer_instance.to_dict()
# create an instance of OfferQueryCancelOffer from a dict
offer_query_cancel_offer_form_dict = offer_query_cancel_offer.from_dict(offer_query_cancel_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


