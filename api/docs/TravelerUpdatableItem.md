# TravelerUpdatableItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**identifier** | **str** | A unique GUID to identify the TravelerUpdatableItem | [optional] 
**addable_ind** | **bool** | If true the TravelerUpdateableItem can be added to the Traveler | [optional] 
**modifiable_ind** | **bool** | If true the TravelerUpdateableItem can be modified in the Traveler | [optional] 
**deletable_ind** | **bool** | If true the TravelerUpdateableItem can be deleted from the Traveler | [optional] 

## Example

```python
from openapi_client.models.traveler_updatable_item import TravelerUpdatableItem

# TODO update the JSON string below
json = "{}"
# create an instance of TravelerUpdatableItem from a JSON string
traveler_updatable_item_instance = TravelerUpdatableItem.from_json(json)
# print the JSON string representation of the object
print TravelerUpdatableItem.to_json()

# convert the object into a dict
traveler_updatable_item_dict = traveler_updatable_item_instance.to_dict()
# create an instance of TravelerUpdatableItem from a dict
traveler_updatable_item_form_dict = traveler_updatable_item.from_dict(traveler_updatable_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


