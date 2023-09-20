# OfferID


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** | Local indentifier within a given message for this object. | [optional] 
**offer_ref** | **str** | Used to reference another instance of this object in the same message | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.offer_id import OfferID

# TODO update the JSON string below
json = "{}"
# create an instance of OfferID from a JSON string
offer_id_instance = OfferID.from_json(json)
# print the JSON string representation of the object
print OfferID.to_json()

# convert the object into a dict
offer_id_dict = offer_id_instance.to_dict()
# create an instance of OfferID from a dict
offer_id_form_dict = offer_id.from_dict(offer_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


