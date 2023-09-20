# ClassOfServiceAvailability

The class of service

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**number** | **int** | The class of service number value | [optional] 
**status** | [**AvailabilityStatusENUM**](AvailabilityStatusENUM.md) |  | [optional] 

## Example

```python
from openapi_client.models.class_of_service_availability import ClassOfServiceAvailability

# TODO update the JSON string below
json = "{}"
# create an instance of ClassOfServiceAvailability from a JSON string
class_of_service_availability_instance = ClassOfServiceAvailability.from_json(json)
# print the JSON string representation of the object
print ClassOfServiceAvailability.to_json()

# convert the object into a dict
class_of_service_availability_dict = class_of_service_availability_instance.to_dict()
# create an instance of ClassOfServiceAvailability from a dict
class_of_service_availability_form_dict = class_of_service_availability.from_dict(class_of_service_availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


