# OrganizationInformation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**organization_identifier** | [**List[OrganizationIdentifier]**](OrganizationIdentifier.md) |  | [optional] 
**gst_registration_number** | [**List[GSTRegistrationNumber]**](GSTRegistrationNumber.md) |  | [optional] 

## Example

```python
from openapi_client.models.organization_information import OrganizationInformation

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationInformation from a JSON string
organization_information_instance = OrganizationInformation.from_json(json)
# print the JSON string representation of the object
print OrganizationInformation.to_json()

# convert the object into a dict
organization_information_dict = organization_information_instance.to_dict()
# create an instance of OrganizationInformation from a dict
organization_information_form_dict = organization_information.from_dict(organization_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


