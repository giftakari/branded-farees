# CompanyName

Identifies a company by name.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**id** | **str** | Use this id to internally identify this company in NextSteps | [optional] 
**division** | **str** | The division name or ID with which the contact is associated | [optional] 
**department** | **str** | The department name or ID with which the contact is associated | [optional] 
**short_name** | **str** | Used to provide the company common name | [optional] 
**code** | **str** | Identifies a company by the company code | [optional] 
**code_context** | **str** | Identifies the context of the identifying code,such as DUNS,IATA or internal code | [optional] 
**system_of_record** | **List[str]** | The system(s) that maintain the data | [optional] 

## Example

```python
from openapi_client.models.company_name import CompanyName

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyName from a JSON string
company_name_instance = CompanyName.from_json(json)
# print the JSON string representation of the object
print CompanyName.to_json()

# convert the object into a dict
company_name_dict = company_name_instance.to_dict()
# create an instance of CompanyName from a dict
company_name_form_dict = company_name.from_dict(company_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


