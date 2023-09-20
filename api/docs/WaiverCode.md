# WaiverCode


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**reason_code** | **int** | A code assigned to identify the reason for disruption | [optional] 

## Example

```python
from openapi_client.models.waiver_code import WaiverCode

# TODO update the JSON string below
json = "{}"
# create an instance of WaiverCode from a JSON string
waiver_code_instance = WaiverCode.from_json(json)
# print the JSON string representation of the object
print WaiverCode.to_json()

# convert the object into a dict
waiver_code_dict = waiver_code_instance.to_dict()
# create an instance of WaiverCode from a dict
waiver_code_form_dict = waiver_code.from_dict(waiver_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


