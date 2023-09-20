# OfferIdentifier


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Local indentifier within a given message for this object. | [optional] 
**offer_ref** | **str** | Used to reference another instance of this object in the same message | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.offer_identifier import OfferIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of OfferIdentifier from a JSON string
offer_identifier_instance = OfferIdentifier.from_json(json)
# print the JSON string representation of the object
print OfferIdentifier.to_json()

# convert the object into a dict
offer_identifier_dict = offer_identifier_instance.to_dict()
# create an instance of OfferIdentifier from a dict
offer_identifier_form_dict = offer_identifier.from_dict(offer_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


