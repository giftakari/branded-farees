# PrimaryContactListRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_contact** | [**List[PrimaryContact]**](PrimaryContact.md) |  | 

## Example

```python
from openapi_client.models.primary_contact_list_request import PrimaryContactListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrimaryContactListRequest from a JSON string
primary_contact_list_request_instance = PrimaryContactListRequest.from_json(json)
# print the JSON string representation of the object
print PrimaryContactListRequest.to_json()

# convert the object into a dict
primary_contact_list_request_dict = primary_contact_list_request_instance.to_dict()
# create an instance of PrimaryContactListRequest from a dict
primary_contact_list_request_form_dict = primary_contact_list_request.from_dict(primary_contact_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


