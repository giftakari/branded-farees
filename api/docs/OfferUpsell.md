# OfferUpsell


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_upsell_ind** | **bool** | If true, the OfferUpsell contains ancillary offerings offered in connection with the ParentOffer | [optional] 

## Example

```python
from openapi_client.models.offer_upsell import OfferUpsell

# TODO update the JSON string below
json = "{}"
# create an instance of OfferUpsell from a JSON string
offer_upsell_instance = OfferUpsell.from_json(json)
# print the JSON string representation of the object
print OfferUpsell.to_json()

# convert the object into a dict
offer_upsell_dict = offer_upsell_instance.to_dict()
# create an instance of OfferUpsell from a dict
offer_upsell_form_dict = offer_upsell.from_dict(offer_upsell_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


