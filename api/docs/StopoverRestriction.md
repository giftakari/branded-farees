# StopoverRestriction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**stopover_charge_ref** | **str** | Reference to the Stopover Charge | 
**journey_types** | [**List[JourneyTypeEnum]**](JourneyTypeEnum.md) |  | [optional] 
**departure_carrier** | **str** | Departure carrier airline code | [optional] 
**arrival_airline** | **str** | Arrival carrier airline code | [optional] 
**geographic_restriction** | [**List[GeographicRestriction]**](GeographicRestriction.md) |  | [optional] 
**online_stopover_only_ind** | **bool** | If true, the stopover may only take place when the arriving and departing airline are the same | [optional] 

## Example

```python
from openapi_client.models.stopover_restriction import StopoverRestriction

# TODO update the JSON string below
json = "{}"
# create an instance of StopoverRestriction from a JSON string
stopover_restriction_instance = StopoverRestriction.from_json(json)
# print the JSON string representation of the object
print StopoverRestriction.to_json()

# convert the object into a dict
stopover_restriction_dict = stopover_restriction_instance.to_dict()
# create an instance of StopoverRestriction from a dict
stopover_restriction_form_dict = stopover_restriction.from_dict(stopover_restriction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


