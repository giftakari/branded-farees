# OriginalIssue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**issuing_city** | **str** | Original Issuing city | 
**issue_date** | **str** | Issue date | 
**agency_code_iata** | **str** | Agency code | 
**document_type** | [**DocumentTypeEnum**](DocumentTypeEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.original_issue import OriginalIssue

# TODO update the JSON string below
json = "{}"
# create an instance of OriginalIssue from a JSON string
original_issue_instance = OriginalIssue.from_json(json)
# print the JSON string representation of the object
print OriginalIssue.to_json()

# convert the object into a dict
original_issue_dict = original_issue_instance.to_dict()
# create an instance of OriginalIssue from a dict
original_issue_form_dict = original_issue.from_dict(original_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


