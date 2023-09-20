# Email

Electronic email addresses, in IETF specified format.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**id** | **str** | Electronic email addresses, in IETF specified format. | [optional] 
**email_type** | **str** | Type of the e-mail | [optional] 
**comment** | **str** | Assigned Type: c-1100:StringText | [optional] 
**preferred_format** | **str** | Mime media type | [optional] 
**share_marketing** | [**YesNoInheritEnum**](YesNoInheritEnum.md) |  | [optional] 
**share_sync** | [**YesNoInheritEnum**](YesNoInheritEnum.md) |  | [optional] 
**opt_out_ind** | [**YesNoInheritEnum**](YesNoInheritEnum.md) |  | [optional] 
**opt_in_status** | [**OptInStatusEnum**](OptInStatusEnum.md) |  | [optional] 
**opt_in_date** | **datetime** | The datetime of receiving the opt in notice | [optional] 
**opt_out_date** | **datetime** | The datetime the opt out notice was received | [optional] 
**valid_ind** | **bool** | If true, this is a valid email address that has been system verified via a successful email transmission. | [optional] 
**provisioned_ind** | **bool** | If true then the email address came from the provisioning process | [optional] 

## Example

```python
from openapi_client.models.email import Email

# TODO update the JSON string below
json = "{}"
# create an instance of Email from a JSON string
email_instance = Email.from_json(json)
# print the JSON string representation of the object
print Email.to_json()

# convert the object into a dict
email_dict = email_instance.to_dict()
# create an instance of Email from a dict
email_form_dict = email.from_dict(email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


