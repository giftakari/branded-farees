# ChangeNotPermitted


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**not_permitted_ind** | **bool** | Changes are not permitted | [optional] 
**penalty_types** | [**List[PenaltyTypeEnum]**](PenaltyTypeEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.change_not_permitted import ChangeNotPermitted

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeNotPermitted from a JSON string
change_not_permitted_instance = ChangeNotPermitted.from_json(json)
# print the JSON string representation of the object
print ChangeNotPermitted.to_json()

# convert the object into a dict
change_not_permitted_dict = change_not_permitted_instance.to_dict()
# create an instance of ChangeNotPermitted from a dict
change_not_permitted_form_dict = change_not_permitted.from_dict(change_not_permitted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


