# VehicleTravelCriteria


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**currency_code** | **str** | Requested currency code | [optional] 
**rate_category** | [**RateCategoryEnum**](RateCategoryEnum.md) |  | [optional] 
**rate_period** | [**RatePeriodEnum**](RatePeriodEnum.md) |  | [optional] 
**unlimited_mileage_ind** | **bool** | If true, this rate includes unlimited mileage | [optional] 
**rate_guaranteed_ind** | **bool** | If true, this rate is guaranteed | [optional] 
**vehicle_date_location** | [**VehicleDateLocation**](VehicleDateLocation.md) |  | [optional] 
**booking_source** | [**Code**](Code.md) |  | [optional] 
**driver_info** | [**DriverInfo**](DriverInfo.md) |  | 
**permitted_vendors** | [**PermittedVendors**](PermittedVendors.md) |  | [optional] 
**prohibited_vendors** | [**ProhibitedVendors**](ProhibitedVendors.md) |  | [optional] 
**rate_code_info** | [**List[RateCodeInfo]**](RateCodeInfo.md) |  | [optional] 
**customer_loyalty** | [**List[CustomerLoyalty]**](CustomerLoyalty.md) |  | [optional] 
**special_equipment** | [**List[SpecialEquipment]**](SpecialEquipment.md) |  | [optional] 
**vehicle_search_modifiers** | [**VehicleSearchModifiers**](VehicleSearchModifiers.md) |  | [optional] 
**search_vehicle_attributes** | [**SearchVehicleAttributes**](SearchVehicleAttributes.md) |  | [optional] 
**vehicle_make_model** | [**List[VehicleMakeModel]**](VehicleMakeModel.md) |  | [optional] 
**next_result_reference** | [**NextResultReference**](NextResultReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.vehicle_travel_criteria import VehicleTravelCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of VehicleTravelCriteria from a JSON string
vehicle_travel_criteria_instance = VehicleTravelCriteria.from_json(json)
# print the JSON string representation of the object
print VehicleTravelCriteria.to_json()

# convert the object into a dict
vehicle_travel_criteria_dict = vehicle_travel_criteria_instance.to_dict()
# create an instance of VehicleTravelCriteria from a dict
vehicle_travel_criteria_form_dict = vehicle_travel_criteria.from_dict(vehicle_travel_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


