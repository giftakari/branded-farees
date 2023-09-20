# FlightType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**connection_type** | [**ConnectionTypeEnum**](ConnectionTypeEnum.md) |  | [optional] 
**exclude_interline_connections_ind** | **bool** | If present and true, exclude interline connections | [optional] 

## Example

```python
from openapi_client.models.flight_type import FlightType

# TODO update the JSON string below
json = "{}"
# create an instance of FlightType from a JSON string
flight_type_instance = FlightType.from_json(json)
# print the JSON string representation of the object
print FlightType.to_json()

# convert the object into a dict
flight_type_dict = flight_type_instance.to_dict()
# create an instance of FlightType from a dict
flight_type_form_dict = flight_type.from_dict(flight_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


