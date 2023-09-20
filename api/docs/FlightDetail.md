# FlightDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability_source_code** | [**AvailabilitySourceCodeENUM**](AvailabilitySourceCodeENUM.md) |  | [optional] 

## Example

```python
from openapi_client.models.flight_detail import FlightDetail

# TODO update the JSON string below
json = "{}"
# create an instance of FlightDetail from a JSON string
flight_detail_instance = FlightDetail.from_json(json)
# print the JSON string representation of the object
print FlightDetail.to_json()

# convert the object into a dict
flight_detail_dict = flight_detail_instance.to_dict()
# create an instance of FlightDetail from a dict
flight_detail_form_dict = flight_detail.from_dict(flight_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


