# OrganizationLoyaltyProgramID


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.organization_loyalty_program_id import OrganizationLoyaltyProgramID

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationLoyaltyProgramID from a JSON string
organization_loyalty_program_id_instance = OrganizationLoyaltyProgramID.from_json(json)
# print the JSON string representation of the object
print OrganizationLoyaltyProgramID.to_json()

# convert the object into a dict
organization_loyalty_program_id_dict = organization_loyalty_program_id_instance.to_dict()
# create an instance of OrganizationLoyaltyProgramID from a dict
organization_loyalty_program_id_form_dict = organization_loyalty_program_id.from_dict(organization_loyalty_program_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


