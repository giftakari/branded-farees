# BuildFromOfferList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**offer_list_identifier** | **str** | The OfferListIdentifer (GUID) to retrieve the OfferList from cache | 
**offer_identifier** | [**List[OfferIdentifier]**](OfferIdentifier.md) |  | 
**product_identifier** | [**List[ProductIdentifier]**](ProductIdentifier.md) |  | [optional] 
**segment_sequence** | **int** | The segmentSequence within the product the action is being requested for. Used when multiple exist within a product | [optional] 

## Example

```python
from openapi_client.models.build_from_offer_list import BuildFromOfferList

# TODO update the JSON string below
json = "{}"
# create an instance of BuildFromOfferList from a JSON string
build_from_offer_list_instance = BuildFromOfferList.from_json(json)
# print the JSON string representation of the object
print BuildFromOfferList.to_json()

# convert the object into a dict
build_from_offer_list_dict = build_from_offer_list_instance.to_dict()
# create an instance of BuildFromOfferList from a dict
build_from_offer_list_form_dict = build_from_offer_list.from_dict(build_from_offer_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


