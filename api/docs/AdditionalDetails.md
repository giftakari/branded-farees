# AdditionalDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**additional_detail** | [**List[AdditionalDetail]**](AdditionalDetail.md) |  | 

## Example

```python
from openapi_client.models.additional_details import AdditionalDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalDetails from a JSON string
additional_details_instance = AdditionalDetails.from_json(json)
# print the JSON string representation of the object
print AdditionalDetails.to_json()

# convert the object into a dict
additional_details_dict = additional_details_instance.to_dict()
# create an instance of AdditionalDetails from a dict
additional_details_form_dict = additional_details.from_dict(additional_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


