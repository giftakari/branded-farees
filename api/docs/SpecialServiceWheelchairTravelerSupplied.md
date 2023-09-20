# SpecialServiceWheelchairTravelerSupplied


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**battery_type_enum** | [**BatteryTypeEnum**](BatteryTypeEnum.md) |  | [optional] 
**measurement** | [**List[Measurement]**](Measurement.md) |  | [optional] 
**cannot_ascend_stairs_ind** | **bool** | if true, traveler needs assistance ascending and descending stairs | [optional] 
**traveler_immobile_ind** | **bool** | if true, traveler is completely immobile and requires assistance to/from aircraft/mobile lounge and ascending/descending stairs | [optional] 

## Example

```python
from openapi_client.models.special_service_wheelchair_traveler_supplied import SpecialServiceWheelchairTravelerSupplied

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialServiceWheelchairTravelerSupplied from a JSON string
special_service_wheelchair_traveler_supplied_instance = SpecialServiceWheelchairTravelerSupplied.from_json(json)
# print the JSON string representation of the object
print SpecialServiceWheelchairTravelerSupplied.to_json()

# convert the object into a dict
special_service_wheelchair_traveler_supplied_dict = special_service_wheelchair_traveler_supplied_instance.to_dict()
# create an instance of SpecialServiceWheelchairTravelerSupplied from a dict
special_service_wheelchair_traveler_supplied_form_dict = special_service_wheelchair_traveler_supplied.from_dict(special_service_wheelchair_traveler_supplied_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


