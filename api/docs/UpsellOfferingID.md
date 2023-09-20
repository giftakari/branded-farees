# UpsellOfferingID


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** | Local indentifier within a given message for this object. | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 
**catalog_product_offering_ref** | **str** | Used to reference another instance of this object in the same message | [optional] 

## Example

```python
from openapi_client.models.upsell_offering_id import UpsellOfferingID

# TODO update the JSON string below
json = "{}"
# create an instance of UpsellOfferingID from a JSON string
upsell_offering_id_instance = UpsellOfferingID.from_json(json)
# print the JSON string representation of the object
print UpsellOfferingID.to_json()

# convert the object into a dict
upsell_offering_id_dict = upsell_offering_id_instance.to_dict()
# create an instance of UpsellOfferingID from a dict
upsell_offering_id_form_dict = upsell_offering_id.from_dict(upsell_offering_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


