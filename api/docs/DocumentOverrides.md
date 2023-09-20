# DocumentOverrides


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_identifier** | [**OfferIdentifier**](OfferIdentifier.md) |  | [optional] 
**product_identifier** | [**ProductIdentifier**](ProductIdentifier.md) |  | [optional] 
**commissions** | [**List[Commissions]**](Commissions.md) |  | [optional] 
**destination_purpose** | [**List[DestinationPurpose]**](DestinationPurpose.md) |  | [optional] 
**restrictions** | [**List[Restrictions]**](Restrictions.md) |  | [optional] 
**tour_codes** | [**List[TourCodes]**](TourCodes.md) |  | [optional] 
**change_fee_collection_method** | [**ChangeFeeCollectionMethod**](ChangeFeeCollectionMethod.md) |  | [optional] 
**net_remit_info** | [**NetRemitInfo**](NetRemitInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.document_overrides import DocumentOverrides

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentOverrides from a JSON string
document_overrides_instance = DocumentOverrides.from_json(json)
# print the JSON string representation of the object
print DocumentOverrides.to_json()

# convert the object into a dict
document_overrides_dict = document_overrides_instance.to_dict()
# create an instance of DocumentOverrides from a dict
document_overrides_form_dict = document_overrides.from_dict(document_overrides_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


