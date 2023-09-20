# TravelerUpdatableItemsID


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** | Internally reference xsd id | [optional] 
**traveler_updatable_items_ref** | **str** |  | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.traveler_updatable_items_id import TravelerUpdatableItemsID

# TODO update the JSON string below
json = "{}"
# create an instance of TravelerUpdatableItemsID from a JSON string
traveler_updatable_items_id_instance = TravelerUpdatableItemsID.from_json(json)
# print the JSON string representation of the object
print TravelerUpdatableItemsID.to_json()

# convert the object into a dict
traveler_updatable_items_id_dict = traveler_updatable_items_id_instance.to_dict()
# create an instance of TravelerUpdatableItemsID from a dict
traveler_updatable_items_id_form_dict = traveler_updatable_items_id.from_dict(traveler_updatable_items_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


