# ProhibitedVendors


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor** | [**List[CompanyName]**](CompanyName.md) |  | 

## Example

```python
from openapi_client.models.prohibited_vendors import ProhibitedVendors

# TODO update the JSON string below
json = "{}"
# create an instance of ProhibitedVendors from a JSON string
prohibited_vendors_instance = ProhibitedVendors.from_json(json)
# print the JSON string representation of the object
print ProhibitedVendors.to_json()

# convert the object into a dict
prohibited_vendors_dict = prohibited_vendors_instance.to_dict()
# create an instance of ProhibitedVendors from a dict
prohibited_vendors_form_dict = prohibited_vendors.from_dict(prohibited_vendors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


