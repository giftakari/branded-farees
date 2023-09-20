# CancelOfferRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_from_offer** | [**BuildFromOffer**](BuildFromOffer.md) |  | [optional] 
**traveler_identifier** | [**List[TravelerIdentifierRef]**](TravelerIdentifierRef.md) |  | [optional] 

## Example

```python
from openapi_client.models.cancel_offer_request import CancelOfferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelOfferRequest from a JSON string
cancel_offer_request_instance = CancelOfferRequest.from_json(json)
# print the JSON string representation of the object
print CancelOfferRequest.to_json()

# convert the object into a dict
cancel_offer_request_dict = cancel_offer_request_instance.to_dict()
# create an instance of CancelOfferRequest from a dict
cancel_offer_request_form_dict = cancel_offer_request.from_dict(cancel_offer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


