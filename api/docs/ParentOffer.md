# ParentOffer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**offer_ref** | **str** |  | [optional] 
**product_ref** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.parent_offer import ParentOffer

# TODO update the JSON string below
json = "{}"
# create an instance of ParentOffer from a JSON string
parent_offer_instance = ParentOffer.from_json(json)
# print the JSON string representation of the object
print ParentOffer.to_json()

# convert the object into a dict
parent_offer_dict = parent_offer_instance.to_dict()
# create an instance of ParentOffer from a dict
parent_offer_form_dict = parent_offer.from_dict(parent_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


