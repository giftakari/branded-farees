# NextStep

A URL that describes a step that can be applied to the resource containing the next step structure.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**id** | **str** | Identifier for the Next Step | [optional] 
**action** | **str** | The action this next step is intended to achieve | 
**method** | [**NextStepMethodEnum**](NextStepMethodEnum.md) |  | 
**description** | **str** | Additional clarification for the next step | [optional] 

## Example

```python
from openapi_client.models.next_step import NextStep

# TODO update the JSON string below
json = "{}"
# create an instance of NextStep from a JSON string
next_step_instance = NextStep.from_json(json)
# print the JSON string representation of the object
print NextStep.to_json()

# convert the object into a dict
next_step_dict = next_step_instance.to_dict()
# create an instance of NextStep from a dict
next_step_form_dict = next_step.from_dict(next_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


