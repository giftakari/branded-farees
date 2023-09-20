# StopoverPermitted


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**journey_types** | [**List[JourneyTypeEnum]**](JourneyTypeEnum.md) |  | [optional] 
**minimum_duration** | **str** | The minimum amount of time permitted for a stopover | 
**maximum_duration** | **str** | The maximum amount of time permitted for a stopover | 
**minimum** | **int** | The minimum permitted for a stopover | 
**maximum** | **int** | The maximum permitted for a stopover | 
**outbound** | **int** | Stopover outbound | [optional] 
**inbound** | **int** | Stopover inbound | [optional] 
**stopover_charge** | [**List[StopoverCharge]**](StopoverCharge.md) |  | 
**stopover_restriction** | [**List[StopoverRestriction]**](StopoverRestriction.md) |  | [optional] 
**permitted_at_gateway_only_ind** | **bool** | If true, stopovers are permitted at gateway points only | [optional] 

## Example

```python
from openapi_client.models.stopover_permitted import StopoverPermitted

# TODO update the JSON string below
json = "{}"
# create an instance of StopoverPermitted from a JSON string
stopover_permitted_instance = StopoverPermitted.from_json(json)
# print the JSON string representation of the object
print StopoverPermitted.to_json()

# convert the object into a dict
stopover_permitted_dict = stopover_permitted_instance.to_dict()
# create an instance of StopoverPermitted from a dict
stopover_permitted_form_dict = stopover_permitted.from_dict(stopover_permitted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


