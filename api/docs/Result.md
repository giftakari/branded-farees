# Result


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**status** | [**ResultStatusEnum**](ResultStatusEnum.md) |  | [optional] 
**error** | [**List[Error]**](Error.md) |  | [optional] 
**warning** | [**List[Warning]**](Warning.md) |  | [optional] 

## Example

```python
from openapi_client.models.result import Result

# TODO update the JSON string below
json = "{}"
# create an instance of Result from a JSON string
result_instance = Result.from_json(json)
# print the JSON string representation of the object
print Result.to_json()

# convert the object into a dict
result_dict = result_instance.to_dict()
# create an instance of Result from a dict
result_form_dict = result.from_dict(result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


