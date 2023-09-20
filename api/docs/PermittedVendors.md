# PermittedVendors


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor** | [**List[CompanyName]**](CompanyName.md) |  | 

## Example

```python
from openapi_client.models.permitted_vendors import PermittedVendors

# TODO update the JSON string below
json = "{}"
# create an instance of PermittedVendors from a JSON string
permitted_vendors_instance = PermittedVendors.from_json(json)
# print the JSON string representation of the object
print PermittedVendors.to_json()

# convert the object into a dict
permitted_vendors_dict = permitted_vendors_instance.to_dict()
# create an instance of PermittedVendors from a dict
permitted_vendors_form_dict = permitted_vendors.from_dict(permitted_vendors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


