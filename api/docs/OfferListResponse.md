# OfferListResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_id** | [**List[OfferID]**](OfferID.md) |  | [optional] 
**transaction_id** | **str** | Unique transaction, correlation or tracking id for a single request and reply i.e. for a single transaction. Should be a 128 bit GUID format. Also know as E2ETrackingId. | [optional] 
**trace_id** | **str** | Optional ID for internal child transactions created for processing a single request (single transaction). Should be a 128 bit GUID format. Also known as ChildTrackingId. | [optional] 
**result** | [**Result**](Result.md) |  | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 
**next_steps** | [**NextSteps**](NextSteps.md) |  | [optional] 
**reference_list** | [**List[ReferenceList]**](ReferenceList.md) |  | [optional] 
**currency_rate_conversion** | [**List[CurrencyRateConversion]**](CurrencyRateConversion.md) |  | [optional] 

## Example

```python
from openapi_client.models.offer_list_response import OfferListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OfferListResponse from a JSON string
offer_list_response_instance = OfferListResponse.from_json(json)
# print the JSON string representation of the object
print OfferListResponse.to_json()

# convert the object into a dict
offer_list_response_dict = offer_list_response_instance.to_dict()
# create an instance of OfferListResponse from a dict
offer_list_response_form_dict = offer_list_response.from_dict(offer_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


