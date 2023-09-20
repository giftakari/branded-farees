# VehicleMakeModel

The make and model of the vehicle along with a description

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**code** | **str** | Assigned Type: c-1100:StringTiny | [optional] 
**supplier_reference** | **str** | Assigned Type: ctvh-1100:SupplierReference | [optional] 
**vendor_code** | **str** | Assigned Type: c-1100:StringTiny | [optional] 
**operating_supplier_code** | **str** | Assigned Type: c-1100:StringTiny | [optional] 
**operating_supplier_name** | **str** | Assigned Type: c-1100:StringTiny | [optional] 

## Example

```python
from openapi_client.models.vehicle_make_model import VehicleMakeModel

# TODO update the JSON string below
json = "{}"
# create an instance of VehicleMakeModel from a JSON string
vehicle_make_model_instance = VehicleMakeModel.from_json(json)
# print the JSON string representation of the object
print VehicleMakeModel.to_json()

# convert the object into a dict
vehicle_make_model_dict = vehicle_make_model_instance.to_dict()
# create an instance of VehicleMakeModel from a dict
vehicle_make_model_form_dict = vehicle_make_model.from_dict(vehicle_make_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


