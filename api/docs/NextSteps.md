# NextSteps


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_uri** | **str** | The base portion of the uri in order to shorten the uri&#39;s in the individual steps | 
**id** | **str** | Optional internally referenced id | [optional] 
**next_step** | [**List[NextStep]**](NextStep.md) |  | 

## Example

```python
from openapi_client.models.next_steps import NextSteps

# TODO update the JSON string below
json = "{}"
# create an instance of NextSteps from a JSON string
next_steps_instance = NextSteps.from_json(json)
# print the JSON string representation of the object
print NextSteps.to_json()

# convert the object into a dict
next_steps_dict = next_steps_instance.to_dict()
# create an instance of NextSteps from a dict
next_steps_form_dict = next_steps.from_dict(next_steps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


