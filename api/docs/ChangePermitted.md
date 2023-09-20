# ChangePermitted


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**penalty_types** | [**List[PenaltyTypeEnum]**](PenaltyTypeEnum.md) |  | 
**penalty_applies_to** | [**PenaltyAppliesToEnum**](PenaltyAppliesToEnum.md) |  | [optional] 
**penalty** | [**List[Penalty]**](Penalty.md) |  | [optional] 
**higher_penatlty_applies_ind** | **bool** | If true, when an amount and a percent are specified in the Penalty then the higher of these apply | [optional] 

## Example

```python
from openapi_client.models.change_permitted import ChangePermitted

# TODO update the JSON string below
json = "{}"
# create an instance of ChangePermitted from a JSON string
change_permitted_instance = ChangePermitted.from_json(json)
# print the JSON string representation of the object
print ChangePermitted.to_json()

# convert the object into a dict
change_permitted_dict = change_permitted_instance.to_dict()
# create an instance of ChangePermitted from a dict
change_permitted_form_dict = change_permitted.from_dict(change_permitted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


