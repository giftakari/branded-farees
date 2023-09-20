# VehicleCharges


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**rate_period** | [**RatePeriodEnum**](RatePeriodEnum.md) |  | [optional] 
**rate_charge_info** | **str** |  | [optional] 
**rate_category** | [**RateCategoryEnum**](RateCategoryEnum.md) |  | [optional] 
**vehicle_coverage_type_code** | [**Code**](Code.md) |  | [optional] 
**calculation** | [**List[Calculation]**](Calculation.md) |  | [optional] 
**vehicle_charge_purpose_code** | [**Code**](Code.md) |  | [optional] 
**tax_inclusive_ind** | **bool** |  | [optional] 
**guaranteed_ind** | **bool** |  | [optional] 
**pay_now_ind** | **bool** | If true the vehicle charge must be paid now and is included in the totalPrice calculation | [optional] 
**included_in_estimated_total_ind** | **bool** |  | [optional] 
**included_in_base_rate_ind** | **bool** | If true the Vehicle Charge has been included in the base rate of the Vehicle price | [optional] 

## Example

```python
from openapi_client.models.vehicle_charges import VehicleCharges

# TODO update the JSON string below
json = "{}"
# create an instance of VehicleCharges from a JSON string
vehicle_charges_instance = VehicleCharges.from_json(json)
# print the JSON string representation of the object
print VehicleCharges.to_json()

# convert the object into a dict
vehicle_charges_dict = vehicle_charges_instance.to_dict()
# create an instance of VehicleCharges from a dict
vehicle_charges_form_dict = vehicle_charges.from_dict(vehicle_charges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


