# TravelerID


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | [optional] 
**traveler_ref** | **str** |  | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.traveler_id import TravelerID

# TODO update the JSON string below
json = "{}"
# create an instance of TravelerID from a JSON string
traveler_id_instance = TravelerID.from_json(json)
# print the JSON string representation of the object
print TravelerID.to_json()

# convert the object into a dict
traveler_id_dict = traveler_id_instance.to_dict()
# create an instance of TravelerID from a dict
traveler_id_form_dict = traveler_id.from_dict(traveler_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


