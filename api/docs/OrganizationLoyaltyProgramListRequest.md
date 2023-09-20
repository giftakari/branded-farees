# OrganizationLoyaltyProgramListRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_loyalty_program** | [**List[OrganizationLoyaltyProgram]**](OrganizationLoyaltyProgram.md) |  | 

## Example

```python
from openapi_client.models.organization_loyalty_program_list_request import OrganizationLoyaltyProgramListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationLoyaltyProgramListRequest from a JSON string
organization_loyalty_program_list_request_instance = OrganizationLoyaltyProgramListRequest.from_json(json)
# print the JSON string representation of the object
print OrganizationLoyaltyProgramListRequest.to_json()

# convert the object into a dict
organization_loyalty_program_list_request_dict = organization_loyalty_program_list_request_instance.to_dict()
# create an instance of OrganizationLoyaltyProgramListRequest from a dict
organization_loyalty_program_list_request_form_dict = organization_loyalty_program_list_request.from_dict(organization_loyalty_program_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


