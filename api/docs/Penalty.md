# Penalty


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**application** | [**CommissionEnum**](CommissionEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.penalty import Penalty

# TODO update the JSON string below
json = "{}"
# create an instance of Penalty from a JSON string
penalty_instance = Penalty.from_json(json)
# print the JSON string representation of the object
print Penalty.to_json()

# convert the object into a dict
penalty_dict = penalty_instance.to_dict()
# create an instance of Penalty from a dict
penalty_form_dict = penalty.from_dict(penalty_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


