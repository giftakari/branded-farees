# OrganizationLoyaltyProgram


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supplier** | **str** | The supplier of the loyalty program | 
**loyalty_identifier** | **str** | Loyalty Identifier | 

## Example

```python
from openapi_client.models.organization_loyalty_program import OrganizationLoyaltyProgram

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationLoyaltyProgram from a JSON string
organization_loyalty_program_instance = OrganizationLoyaltyProgram.from_json(json)
# print the JSON string representation of the object
print OrganizationLoyaltyProgram.to_json()

# convert the object into a dict
organization_loyalty_program_dict = organization_loyalty_program_instance.to_dict()
# create an instance of OrganizationLoyaltyProgram from a dict
organization_loyalty_program_form_dict = organization_loyalty_program.from_dict(organization_loyalty_program_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


