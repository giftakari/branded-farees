# FirstReservation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**time_of_day** | **str** | The time of day indicates the earliest time the Offer can be reserved. Used in conjunction with DayOfWeek or Duration | [optional] 

## Example

```python
from openapi_client.models.first_reservation import FirstReservation

# TODO update the JSON string below
json = "{}"
# create an instance of FirstReservation from a JSON string
first_reservation_instance = FirstReservation.from_json(json)
# print the JSON string representation of the object
print FirstReservation.to_json()

# convert the object into a dict
first_reservation_dict = first_reservation_instance.to_dict()
# create an instance of FirstReservation from a dict
first_reservation_form_dict = first_reservation.from_dict(first_reservation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


