# Offer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_offer_ref** | **str** | A reference to the Offer this offer is sold in conjunction with | [optional] 
**product** | [**List[ProductID]**](ProductID.md) |  | 
**price** | [**Price**](Price.md) |  | 
**terms_and_conditions_full** | [**List[TermsAndConditionsFull]**](TermsAndConditionsFull.md) |  | 
**passive_offer_ind** | **bool** | If true, the Offer is passive for booking purposes. | [optional] 

## Example

```python
from openapi_client.models.offer import Offer

# TODO update the JSON string below
json = "{}"
# create an instance of Offer from a JSON string
offer_instance = Offer.from_json(json)
# print the JSON string representation of the object
print Offer.to_json()

# convert the object into a dict
offer_dict = offer_instance.to_dict()
# create an instance of Offer from a dict
offer_form_dict = offer.from_dict(offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


