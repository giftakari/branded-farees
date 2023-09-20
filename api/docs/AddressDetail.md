# AddressDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_type** | **str** | OTA code for address type | [optional] 
**use** | **str** | OTA code for address use | [optional] 
**comment** | [**Comment**](Comment.md) |  | [optional] 
**privacy** | [**Privacy**](Privacy.md) |  | [optional] 
**priority** | **int** | The priority ranking within the group | [optional] 
**valid_ind** | **bool** | If true, this is a valid and complete mailing address that has been verified through an address verification service or previously mailed materials have not been returned. | [optional] 
**provisioned_ind** | **bool** | If true, this address came into the system through provisioning | [optional] 

## Example

```python
from openapi_client.models.address_detail import AddressDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AddressDetail from a JSON string
address_detail_instance = AddressDetail.from_json(json)
# print the JSON string representation of the object
print AddressDetail.to_json()

# convert the object into a dict
address_detail_dict = address_detail_instance.to_dict()
# create an instance of AddressDetail from a dict
address_detail_form_dict = address_detail.from_dict(address_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


