# CancelPermitted


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**penalty_types** | [**List[PenaltyTypeEnum]**](PenaltyTypeEnum.md) |  | 
**penalty_applies_to** | [**PenaltyAppliesToEnum**](PenaltyAppliesToEnum.md) |  | [optional] 
**penalty** | [**List[Penalty]**](Penalty.md) |  | [optional] 
**higher_penatlty_applies_ind** | **bool** | If true, when an amount and a percent are specified in the Penalty then the higher of these apply | [optional] 

## Example

```python
from openapi_client.models.cancel_permitted import CancelPermitted

# TODO update the JSON string below
json = "{}"
# create an instance of CancelPermitted from a JSON string
cancel_permitted_instance = CancelPermitted.from_json(json)
# print the JSON string representation of the object
print CancelPermitted.to_json()

# convert the object into a dict
cancel_permitted_dict = cancel_permitted_instance.to_dict()
# create an instance of CancelPermitted from a dict
cancel_permitted_form_dict = cancel_permitted.from_dict(cancel_permitted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


