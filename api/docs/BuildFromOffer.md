# BuildFromOffer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**offer_identifier** | [**OfferIdentifier**](OfferIdentifier.md) |  | 
**product_identifier** | [**List[ProductIdentifier]**](ProductIdentifier.md) |  | [optional] 
**payment_criteria** | [**PaymentCriteria**](PaymentCriteria.md) |  | [optional] 

## Example

```python
from openapi_client.models.build_from_offer import BuildFromOffer

# TODO update the JSON string below
json = "{}"
# create an instance of BuildFromOffer from a JSON string
build_from_offer_instance = BuildFromOffer.from_json(json)
# print the JSON string representation of the object
print BuildFromOffer.to_json()

# convert the object into a dict
build_from_offer_dict = build_from_offer_instance.to_dict()
# create an instance of BuildFromOffer from a dict
build_from_offer_form_dict = build_from_offer.from_dict(build_from_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


