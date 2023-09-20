# PreviousIssue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**issuing_city** | **str** |  | [optional] 
**issue_date** | **str** |  | [optional] 
**agency_code_iata** | **str** |  | [optional] 
**document_type** | [**DocumentTypeEnum**](DocumentTypeEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.previous_issue import PreviousIssue

# TODO update the JSON string below
json = "{}"
# create an instance of PreviousIssue from a JSON string
previous_issue_instance = PreviousIssue.from_json(json)
# print the JSON string representation of the object
print PreviousIssue.to_json()

# convert the object into a dict
previous_issue_dict = previous_issue_instance.to_dict()
# create an instance of PreviousIssue from a dict
previous_issue_form_dict = previous_issue.from_dict(previous_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


