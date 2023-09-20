# TravelerUpdatedItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**traveler_updatable_item_id** | **str** | A unique GUID to identify the TravelerUpdatedItem | [optional] 
**add_ind** | **bool** | If true the TravelerUpdatedItem is being added to the Traveler | [optional] 
**modify_ind** | **bool** | If true the TravelerUpdatedItem is being modified in the Traveler | [optional] 
**delete_ind** | **bool** | If true the TravelerUpdatedItem is being deleted from the Traveler | [optional] 

## Example

```python
from openapi_client.models.traveler_updated_item import TravelerUpdatedItem

# TODO update the JSON string below
json = "{}"
# create an instance of TravelerUpdatedItem from a JSON string
traveler_updated_item_instance = TravelerUpdatedItem.from_json(json)
# print the JSON string representation of the object
print TravelerUpdatedItem.to_json()

# convert the object into a dict
traveler_updated_item_dict = traveler_updated_item_instance.to_dict()
# create an instance of TravelerUpdatedItem from a dict
traveler_updated_item_form_dict = traveler_updated_item.from_dict(traveler_updated_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


