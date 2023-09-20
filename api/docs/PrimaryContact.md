# PrimaryContact


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**share_with** | [**ShareWithEnum**](ShareWithEnum.md) |  | [optional] 
**share_with_supplier** | **List[str]** | Primary contact shared with supplier | [optional] 
**email** | [**Email**](Email.md) |  | [optional] 
**telephone** | [**Telephone**](Telephone.md) |  | [optional] 
**traveler_identifier** | [**TravelerIdentifier**](TravelerIdentifier.md) |  | [optional] 
**contact_information_refused_ind** | **bool** | If true, the passenger has refused to provide emergency contact details | [optional] 

## Example

```python
from openapi_client.models.primary_contact import PrimaryContact

# TODO update the JSON string below
json = "{}"
# create an instance of PrimaryContact from a JSON string
primary_contact_instance = PrimaryContact.from_json(json)
# print the JSON string representation of the object
print PrimaryContact.to_json()

# convert the object into a dict
primary_contact_dict = primary_contact_instance.to_dict()
# create an instance of PrimaryContact from a dict
primary_contact_form_dict = primary_contact.from_dict(primary_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


