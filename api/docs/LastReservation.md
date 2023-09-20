# LastReservation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**time_of_day** | **str** | The time of day indicates the earliest time the Offer can be reserved. Used in conjunction with DayOfWeek or Duration | [optional] 

## Example

```python
from openapi_client.models.last_reservation import LastReservation

# TODO update the JSON string below
json = "{}"
# create an instance of LastReservation from a JSON string
last_reservation_instance = LastReservation.from_json(json)
# print the JSON string representation of the object
print LastReservation.to_json()

# convert the object into a dict
last_reservation_dict = last_reservation_instance.to_dict()
# create an instance of LastReservation from a dict
last_reservation_form_dict = last_reservation.from_dict(last_reservation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


