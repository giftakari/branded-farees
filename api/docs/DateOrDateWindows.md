# DateOrDateWindows

Indicates the expiry date.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specific** | **date** | A specific date. When used with a windows must fall between start and end. | [optional] 
**start** | **date** | The earliest and latest dates acceptable for the start date. | [optional] 
**end** | **date** | The earliest and latest dates acceptable for the end date. | [optional] 
**duration** | **str** | Duration from  start date. | [optional] 
**duration_unit** | [**DurationUnitEnum**](DurationUnitEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.date_or_date_windows import DateOrDateWindows

# TODO update the JSON string below
json = "{}"
# create an instance of DateOrDateWindows from a JSON string
date_or_date_windows_instance = DateOrDateWindows.from_json(json)
# print the JSON string representation of the object
print DateOrDateWindows.to_json()

# convert the object into a dict
date_or_date_windows_dict = date_or_date_windows_instance.to_dict()
# create an instance of DateOrDateWindows from a dict
date_or_date_windows_form_dict = date_or_date_windows.from_dict(date_or_date_windows_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


