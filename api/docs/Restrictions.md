# Restrictions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**traveler_identifier_ref** | [**List[TravelerIdentifierRef]**](TravelerIdentifierRef.md) |  | [optional] 
**restriction** | **List[str]** |  | 
**document_type** | [**DocumentTypeEnum**](DocumentTypeEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.restrictions import Restrictions

# TODO update the JSON string below
json = "{}"
# create an instance of Restrictions from a JSON string
restrictions_instance = Restrictions.from_json(json)
# print the JSON string representation of the object
print Restrictions.to_json()

# convert the object into a dict
restrictions_dict = restrictions_instance.to_dict()
# create an instance of Restrictions from a dict
restrictions_form_dict = restrictions.from_dict(restrictions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


