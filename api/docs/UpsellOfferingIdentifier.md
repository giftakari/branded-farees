# UpsellOfferingIdentifier


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Local indentifier within a given message for this object. | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 
**catalog_product_offering_ref** | **str** | Used to reference another instance of this object in the same message | [optional] 

## Example

```python
from openapi_client.models.upsell_offering_identifier import UpsellOfferingIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of UpsellOfferingIdentifier from a JSON string
upsell_offering_identifier_instance = UpsellOfferingIdentifier.from_json(json)
# print the JSON string representation of the object
print UpsellOfferingIdentifier.to_json()

# convert the object into a dict
upsell_offering_identifier_dict = upsell_offering_identifier_instance.to_dict()
# create an instance of UpsellOfferingIdentifier from a dict
upsell_offering_identifier_form_dict = upsell_offering_identifier.from_dict(upsell_offering_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


