# DateEffectiveExpire

Used to identify the effective date and/or expiration date.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective** | **date** | Indicates the starting date. | [optional] 
**expire** | **date** | Indicates the ending date. | [optional] 
**expire_date_exclusive_ind** | **bool** | When true, indicates that the ExpireDate is the first day after the applicable period (e.g. when expire date is Oct 15  the last date of the period is Oct 14). | [optional] 

## Example

```python
from openapi_client.models.date_effective_expire import DateEffectiveExpire

# TODO update the JSON string below
json = "{}"
# create an instance of DateEffectiveExpire from a JSON string
date_effective_expire_instance = DateEffectiveExpire.from_json(json)
# print the JSON string representation of the object
print DateEffectiveExpire.to_json()

# convert the object into a dict
date_effective_expire_dict = date_effective_expire_instance.to_dict()
# create an instance of DateEffectiveExpire from a dict
date_effective_expire_form_dict = date_effective_expire.from_dict(date_effective_expire_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


