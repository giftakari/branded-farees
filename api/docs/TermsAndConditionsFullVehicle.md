# TermsAndConditionsFullVehicle


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terms_and_conditions_sub_category** | [**TextBlock**](TextBlock.md) |  | [optional] 
**driver_info** | [**DriverInfo**](DriverInfo.md) |  | [optional] 
**product_rate_code_info** | [**List[ProductRateCodeInfo]**](ProductRateCodeInfo.md) |  | [optional] 
**policy** | [**Policy**](Policy.md) |  | [optional] 
**flight_restriction_ind** | **bool** | if true, the traveler must have a valid flight to qualify for this Offer | [optional] 

## Example

```python
from openapi_client.models.terms_and_conditions_full_vehicle import TermsAndConditionsFullVehicle

# TODO update the JSON string below
json = "{}"
# create an instance of TermsAndConditionsFullVehicle from a JSON string
terms_and_conditions_full_vehicle_instance = TermsAndConditionsFullVehicle.from_json(json)
# print the JSON string representation of the object
print TermsAndConditionsFullVehicle.to_json()

# convert the object into a dict
terms_and_conditions_full_vehicle_dict = terms_and_conditions_full_vehicle_instance.to_dict()
# create an instance of TermsAndConditionsFullVehicle from a dict
terms_and_conditions_full_vehicle_form_dict = terms_and_conditions_full_vehicle.from_dict(terms_and_conditions_full_vehicle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


