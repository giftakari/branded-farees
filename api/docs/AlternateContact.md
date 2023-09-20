# AlternateContact


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**contact_type** | **str** | Contact type value | [optional] 
**relation** | **str** | Relation value | [optional] 
**person_name** | [**PersonName**](PersonName.md) |  | 
**address** | [**List[Address]**](Address.md) |  | [optional] 
**telephone** | [**List[Telephone]**](Telephone.md) |  | [optional] 
**email** | [**List[Email]**](Email.md) |  | [optional] 
**emergency_ind** | **bool** | This is the contact in case of an emergency | [optional] 
**default_ind** | **bool** | This is the default contact | [optional] 

## Example

```python
from openapi_client.models.alternate_contact import AlternateContact

# TODO update the JSON string below
json = "{}"
# create an instance of AlternateContact from a JSON string
alternate_contact_instance = AlternateContact.from_json(json)
# print the JSON string representation of the object
print AlternateContact.to_json()

# convert the object into a dict
alternate_contact_dict = alternate_contact_instance.to_dict()
# create an instance of AlternateContact from a dict
alternate_contact_form_dict = alternate_contact.from_dict(alternate_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


