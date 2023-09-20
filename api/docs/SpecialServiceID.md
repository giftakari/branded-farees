# SpecialServiceID


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** | Internal Id | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.special_service_id import SpecialServiceID

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialServiceID from a JSON string
special_service_id_instance = SpecialServiceID.from_json(json)
# print the JSON string representation of the object
print SpecialServiceID.to_json()

# convert the object into a dict
special_service_id_dict = special_service_id_instance.to_dict()
# create an instance of SpecialServiceID from a dict
special_service_id_form_dict = special_service_id.from_dict(special_service_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


