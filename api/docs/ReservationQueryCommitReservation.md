# ReservationQueryCommitReservation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification** | [**List[Notification]**](Notification.md) |  | [optional] 
**schedule_change_accepted_ind** | **bool** | if true, the schedule change is accepted by the consumer | [optional] 
**error_when_offer_price_cancelled_ind** | **bool** | If true, and the OfferPrice is invalidated, error will be returned and Reservation commit will not be processed | [optional] 
**schedule_change_reprice** | [**ScheduleChangeRepriceEnum**](ScheduleChangeRepriceEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.reservation_query_commit_reservation import ReservationQueryCommitReservation

# TODO update the JSON string below
json = "{}"
# create an instance of ReservationQueryCommitReservation from a JSON string
reservation_query_commit_reservation_instance = ReservationQueryCommitReservation.from_json(json)
# print the JSON string representation of the object
print ReservationQueryCommitReservation.to_json()

# convert the object into a dict
reservation_query_commit_reservation_dict = reservation_query_commit_reservation_instance.to_dict()
# create an instance of ReservationQueryCommitReservation from a dict
reservation_query_commit_reservation_form_dict = reservation_query_commit_reservation.from_dict(reservation_query_commit_reservation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


