# PenaltySourceCode


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**code_context** | **str** | Penalty source code context | [optional] 

## Example

```python
from openapi_client.models.penalty_source_code import PenaltySourceCode

# TODO update the JSON string below
json = "{}"
# create an instance of PenaltySourceCode from a JSON string
penalty_source_code_instance = PenaltySourceCode.from_json(json)
# print the JSON string representation of the object
print PenaltySourceCode.to_json()

# convert the object into a dict
penalty_source_code_dict = penalty_source_code_instance.to_dict()
# create an instance of PenaltySourceCode from a dict
penalty_source_code_form_dict = penalty_source_code.from_dict(penalty_source_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


