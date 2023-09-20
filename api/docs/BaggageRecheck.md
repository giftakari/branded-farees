# BaggageRecheck


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**at** | **str** | The city where the baggage recheck is required | 
**arrival_flight** | [**FlightID**](FlightID.md) |  | 
**departure_flight** | [**FlightID**](FlightID.md) |  | 

## Example

```python
from openapi_client.models.baggage_recheck import BaggageRecheck

# TODO update the JSON string below
json = "{}"
# create an instance of BaggageRecheck from a JSON string
baggage_recheck_instance = BaggageRecheck.from_json(json)
# print the JSON string representation of the object
print BaggageRecheck.to_json()

# convert the object into a dict
baggage_recheck_dict = baggage_recheck_instance.to_dict()
# create an instance of BaggageRecheck from a dict
baggage_recheck_form_dict = baggage_recheck.from_dict(baggage_recheck_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


