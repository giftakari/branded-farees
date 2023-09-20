# VehicleDateLocation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**rental_pickup** | [**RentalPickupReturn**](RentalPickupReturn.md) |  | 
**rental_return** | [**RentalPickupReturn**](RentalPickupReturn.md) |  | 

## Example

```python
from openapi_client.models.vehicle_date_location import VehicleDateLocation

# TODO update the JSON string below
json = "{}"
# create an instance of VehicleDateLocation from a JSON string
vehicle_date_location_instance = VehicleDateLocation.from_json(json)
# print the JSON string representation of the object
print VehicleDateLocation.to_json()

# convert the object into a dict
vehicle_date_location_dict = vehicle_date_location_instance.to_dict()
# create an instance of VehicleDateLocation from a dict
vehicle_date_location_form_dict = vehicle_date_location.from_dict(vehicle_date_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


