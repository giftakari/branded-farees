# VehicleDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vehicle_date_location** | [**VehicleDateLocation**](VehicleDateLocation.md) |  | [optional] 

## Example

```python
from openapi_client.models.vehicle_detail import VehicleDetail

# TODO update the JSON string below
json = "{}"
# create an instance of VehicleDetail from a JSON string
vehicle_detail_instance = VehicleDetail.from_json(json)
# print the JSON string representation of the object
print VehicleDetail.to_json()

# convert the object into a dict
vehicle_detail_dict = vehicle_detail_instance.to_dict()
# create an instance of VehicleDetail from a dict
vehicle_detail_form_dict = vehicle_detail.from_dict(vehicle_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


