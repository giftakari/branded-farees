# EMDQueryUpdateEMD


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**agency_code** | **str** | Assigned Type: c-1100:AgencyCodeIATA | [optional] 
**status** | **str** | Assigned Type: c-1100:StringTiny | 
**date_of_issue** | **date** | The date the EMD was issued | [optional] 

## Example

```python
from openapi_client.models.emd_query_update_emd import EMDQueryUpdateEMD

# TODO update the JSON string below
json = "{}"
# create an instance of EMDQueryUpdateEMD from a JSON string
emd_query_update_emd_instance = EMDQueryUpdateEMD.from_json(json)
# print the JSON string representation of the object
print EMDQueryUpdateEMD.to_json()

# convert the object into a dict
emd_query_update_emd_dict = emd_query_update_emd_instance.to_dict()
# create an instance of EMDQueryUpdateEMD from a dict
emd_query_update_emd_form_dict = emd_query_update_emd.from_dict(emd_query_update_emd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


