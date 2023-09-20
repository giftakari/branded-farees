# ProductAncillaryVehicle


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**equipment_type_code** | [**Code**](Code.md) |  | [optional] 
**free_quantity_included_in_price** | **int** | The mount of this ancillary that is included with the vehicle rental | [optional] 
**max_bookable_quantity** | **int** | The maximum amount of this ancillary that may be booked with the vehicle rental | [optional] 

## Example

```python
from openapi_client.models.product_ancillary_vehicle import ProductAncillaryVehicle

# TODO update the JSON string below
json = "{}"
# create an instance of ProductAncillaryVehicle from a JSON string
product_ancillary_vehicle_instance = ProductAncillaryVehicle.from_json(json)
# print the JSON string representation of the object
print ProductAncillaryVehicle.to_json()

# convert the object into a dict
product_ancillary_vehicle_dict = product_ancillary_vehicle_instance.to_dict()
# create an instance of ProductAncillaryVehicle from a dict
product_ancillary_vehicle_form_dict = product_ancillary_vehicle.from_dict(product_ancillary_vehicle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


