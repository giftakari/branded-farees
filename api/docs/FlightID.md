# FlightID


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** | Internal ID | [optional] 
**flight_ref** | **str** | Reference to a Flight object eslewhere in the message | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.flight_id import FlightID

# TODO update the JSON string below
json = "{}"
# create an instance of FlightID from a JSON string
flight_id_instance = FlightID.from_json(json)
# print the JSON string representation of the object
print FlightID.to_json()

# convert the object into a dict
flight_id_dict = flight_id_instance.to_dict()
# create an instance of FlightID from a dict
flight_id_form_dict = flight_id.from_dict(flight_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


