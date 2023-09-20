# TelephoneDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_location_type** | **str** | Location of the phone | [optional] 
**phone_tech_type** | **str** | Indicates the type of technology associated with the telephone number | [optional] 
**phone_use_type** | **str** | Use of the phone | [optional] 
**pin** | **str** | Additional codes used for telephone | [optional] 
**priority** | **int** | Priority | [optional] 
**privacy** | [**Privacy**](Privacy.md) |  | [optional] 
**enum_telephone_role** | [**EnumTelephoneRole**](EnumTelephoneRole.md) |  | [optional] 
**comment** | [**Comment**](Comment.md) |  | [optional] 
**default_ind** | **bool** | When true, indicates a default value should be used. | [optional] 
**provisioned_ind** | **bool** | true indicates this phone number was created through provisioned | [optional] 

## Example

```python
from openapi_client.models.telephone_detail import TelephoneDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TelephoneDetail from a JSON string
telephone_detail_instance = TelephoneDetail.from_json(json)
# print the JSON string representation of the object
print TelephoneDetail.to_json()

# convert the object into a dict
telephone_detail_dict = telephone_detail_instance.to_dict()
# create an instance of TelephoneDetail from a dict
telephone_detail_form_dict = telephone_detail.from_dict(telephone_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


