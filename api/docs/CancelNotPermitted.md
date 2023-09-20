# CancelNotPermitted


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**not_permitted_ind** | **bool** | Changes are not permitted | [optional] 
**penalty_types** | [**List[PenaltyTypeEnum]**](PenaltyTypeEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.cancel_not_permitted import CancelNotPermitted

# TODO update the JSON string below
json = "{}"
# create an instance of CancelNotPermitted from a JSON string
cancel_not_permitted_instance = CancelNotPermitted.from_json(json)
# print the JSON string representation of the object
print CancelNotPermitted.to_json()

# convert the object into a dict
cancel_not_permitted_dict = cancel_not_permitted_instance.to_dict()
# create an instance of CancelNotPermitted from a dict
cancel_not_permitted_form_dict = cancel_not_permitted.from_dict(cancel_not_permitted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


