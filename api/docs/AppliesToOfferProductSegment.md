# AppliesToOfferProductSegment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_identifier** | [**OfferIdentifier**](OfferIdentifier.md) |  | [optional] 
**product_identifier** | [**ProductIdentifier**](ProductIdentifier.md) |  | [optional] 
**segment_sequence_list** | **List[int]** | Segment Sequence List | [optional] 

## Example

```python
from openapi_client.models.applies_to_offer_product_segment import AppliesToOfferProductSegment

# TODO update the JSON string below
json = "{}"
# create an instance of AppliesToOfferProductSegment from a JSON string
applies_to_offer_product_segment_instance = AppliesToOfferProductSegment.from_json(json)
# print the JSON string representation of the object
print AppliesToOfferProductSegment.to_json()

# convert the object into a dict
applies_to_offer_product_segment_dict = applies_to_offer_product_segment_instance.to_dict()
# create an instance of AppliesToOfferProductSegment from a dict
applies_to_offer_product_segment_form_dict = applies_to_offer_product_segment.from_dict(applies_to_offer_product_segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


