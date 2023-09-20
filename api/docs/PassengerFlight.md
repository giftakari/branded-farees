# PassengerFlight


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**passenger_quantity** | **int** | Number of passengers of the specified passenger type code | [optional] 
**passenger_type_code** | **str** | Passenger type code | [optional] 
**flight_product** | [**List[FlightProduct]**](FlightProduct.md) |  | [optional] 

## Example

```python
from openapi_client.models.passenger_flight import PassengerFlight

# TODO update the JSON string below
json = "{}"
# create an instance of PassengerFlight from a JSON string
passenger_flight_instance = PassengerFlight.from_json(json)
# print the JSON string representation of the object
print PassengerFlight.to_json()

# convert the object into a dict
passenger_flight_dict = passenger_flight_instance.to_dict()
# create an instance of PassengerFlight from a dict
passenger_flight_form_dict = passenger_flight.from_dict(passenger_flight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


