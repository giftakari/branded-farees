# NextResultReference

Container to return/send additional search results

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**provider_code** | **str** | Assigned Type: c-1100:SupplierCode | [optional] 

## Example

```python
from openapi_client.models.next_result_reference import NextResultReference

# TODO update the JSON string below
json = "{}"
# create an instance of NextResultReference from a JSON string
next_result_reference_instance = NextResultReference.from_json(json)
# print the JSON string representation of the object
print NextResultReference.to_json()

# convert the object into a dict
next_result_reference_dict = next_result_reference_instance.to_dict()
# create an instance of NextResultReference from a dict
next_result_reference_form_dict = next_result_reference.from_dict(next_result_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


