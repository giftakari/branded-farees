# ReservationQuerySearchCriteriaReservation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**person_name** | [**PersonName**](PersonName.md) |  | [optional] 
**departure_date** | **date** | Local date of flight departure | [optional] 
**departure_date_range** | [**DateRange**](DateRange.md) |  | [optional] 
**departure** | **str** | The city or airport code a flight is departing from in the Reservation | [optional] 
**arrival** | **str** | The city or airport code a flight is arriving at in the Reservation | [optional] 
**detail_view_ind** | **bool** | If true, ReservationDetail will be returned | [optional] 

## Example

```python
from openapi_client.models.reservation_query_search_criteria_reservation import ReservationQuerySearchCriteriaReservation

# TODO update the JSON string below
json = "{}"
# create an instance of ReservationQuerySearchCriteriaReservation from a JSON string
reservation_query_search_criteria_reservation_instance = ReservationQuerySearchCriteriaReservation.from_json(json)
# print the JSON string representation of the object
print ReservationQuerySearchCriteriaReservation.to_json()

# convert the object into a dict
reservation_query_search_criteria_reservation_dict = reservation_query_search_criteria_reservation_instance.to_dict()
# create an instance of ReservationQuerySearchCriteriaReservation from a dict
reservation_query_search_criteria_reservation_form_dict = reservation_query_search_criteria_reservation.from_dict(reservation_query_search_criteria_reservation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


