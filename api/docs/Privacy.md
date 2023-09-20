# Privacy

Confidential details for marketing purpose

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Optional internally referenced id | [optional] 
**share_marketing** | [**YesNoInheritEnum**](YesNoInheritEnum.md) |  | [optional] 
**share_sync** | [**YesNoInheritEnum**](YesNoInheritEnum.md) |  | [optional] 
**opt_out_ind** | [**YesNoInheritEnum**](YesNoInheritEnum.md) |  | [optional] 
**opt_in_status** | [**OptInStatusEnum**](OptInStatusEnum.md) |  | [optional] 
**opt_in_date** | **datetime** | The datetime of receiving the opt in notice | [optional] 
**opt_out_date** | **datetime** | The datetime the opt out notice was received | [optional] 

## Example

```python
from openapi_client.models.privacy import Privacy

# TODO update the JSON string below
json = "{}"
# create an instance of Privacy from a JSON string
privacy_instance = Privacy.from_json(json)
# print the JSON string representation of the object
print Privacy.to_json()

# convert the object into a dict
privacy_dict = privacy_instance.to_dict()
# create an instance of Privacy from a dict
privacy_form_dict = privacy.from_dict(privacy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


