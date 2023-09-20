# ProductAir


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_duration** | **str** | Total duration of all Segments that are part of this ProductAir | [optional] 
**flight_segment** | [**List[FlightSegment]**](FlightSegment.md) |  | 
**passenger_flight** | [**List[PassengerFlight]**](PassengerFlight.md) |  | 

## Example

```python
from openapi_client.models.product_air import ProductAir

# TODO update the JSON string below
json = "{}"
# create an instance of ProductAir from a JSON string
product_air_instance = ProductAir.from_json(json)
# print the JSON string representation of the object
print ProductAir.to_json()

# convert the object into a dict
product_air_dict = product_air_instance.to_dict()
# create an instance of ProductAir from a dict
product_air_form_dict = product_air.from_dict(product_air_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


