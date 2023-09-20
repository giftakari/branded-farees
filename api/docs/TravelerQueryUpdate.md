# TravelerQueryUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**traveler_updated_item** | [**List[TravelerUpdatedItem]**](TravelerUpdatedItem.md) |  | 

## Example

```python
from openapi_client.models.traveler_query_update import TravelerQueryUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of TravelerQueryUpdate from a JSON string
traveler_query_update_instance = TravelerQueryUpdate.from_json(json)
# print the JSON string representation of the object
print TravelerQueryUpdate.to_json()

# convert the object into a dict
traveler_query_update_dict = traveler_query_update_instance.to_dict()
# create an instance of TravelerQueryUpdate from a dict
traveler_query_update_form_dict = traveler_query_update.from_dict(traveler_query_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


