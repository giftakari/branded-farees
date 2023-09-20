# DriverInfo

Basic information (metadata) about the intended driver of the vehicle

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age** | **int** | Assigned Type: c-1100:NumberDoubleDigit | [optional] 
**country_of_doc_issue** | **str** | Assigned Type: c-1100:CountryCodeISO | [optional] 

## Example

```python
from openapi_client.models.driver_info import DriverInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DriverInfo from a JSON string
driver_info_instance = DriverInfo.from_json(json)
# print the JSON string representation of the object
print DriverInfo.to_json()

# convert the object into a dict
driver_info_dict = driver_info_instance.to_dict()
# create an instance of DriverInfo from a dict
driver_info_form_dict = driver_info.from_dict(driver_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


