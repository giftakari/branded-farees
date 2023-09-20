# ReservationBuildVehicle


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vehicle_travel_criteria** | [**VehicleTravelCriteria**](VehicleTravelCriteria.md) |  | [optional] 
**arrival_details** | [**ArrivalDetails**](ArrivalDetails.md) |  | [optional] 

## Example

```python
from openapi_client.models.reservation_build_vehicle import ReservationBuildVehicle

# TODO update the JSON string below
json = "{}"
# create an instance of ReservationBuildVehicle from a JSON string
reservation_build_vehicle_instance = ReservationBuildVehicle.from_json(json)
# print the JSON string representation of the object
print ReservationBuildVehicle.to_json()

# convert the object into a dict
reservation_build_vehicle_dict = reservation_build_vehicle_instance.to_dict()
# create an instance of ReservationBuildVehicle from a dict
reservation_build_vehicle_form_dict = reservation_build_vehicle.from_dict(reservation_build_vehicle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


