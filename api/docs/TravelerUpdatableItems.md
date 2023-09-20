# TravelerUpdatableItems


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**traveler_identifier** | **str** | Traveler identifier value | [optional] 
**traveler_updatable_item** | [**List[TravelerUpdatableItem]**](TravelerUpdatableItem.md) |  | [optional] 

## Example

```python
from openapi_client.models.traveler_updatable_items import TravelerUpdatableItems

# TODO update the JSON string below
json = "{}"
# create an instance of TravelerUpdatableItems from a JSON string
traveler_updatable_items_instance = TravelerUpdatableItems.from_json(json)
# print the JSON string representation of the object
print TravelerUpdatableItems.to_json()

# convert the object into a dict
traveler_updatable_items_dict = traveler_updatable_items_instance.to_dict()
# create an instance of TravelerUpdatableItems from a dict
traveler_updatable_items_form_dict = traveler_updatable_items.from_dict(traveler_updatable_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


