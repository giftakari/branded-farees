# OfferLink


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**offer_ref** | **str** |  | [optional] 
**parent_offer** | [**ParentOffer**](ParentOffer.md) |  | [optional] 

## Example

```python
from openapi_client.models.offer_link import OfferLink

# TODO update the JSON string below
json = "{}"
# create an instance of OfferLink from a JSON string
offer_link_instance = OfferLink.from_json(json)
# print the JSON string representation of the object
print OfferLink.to_json()

# convert the object into a dict
offer_link_dict = offer_link_instance.to_dict()
# create an instance of OfferLink from a dict
offer_link_form_dict = offer_link.from_dict(offer_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


