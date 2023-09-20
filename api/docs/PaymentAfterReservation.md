# PaymentAfterReservation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**time_of_day** | **str** | The time of day indicates the earliest time the Offer can be reserved. Used in conjunction with DayOfWeek or Duration | [optional] 

## Example

```python
from openapi_client.models.payment_after_reservation import PaymentAfterReservation

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentAfterReservation from a JSON string
payment_after_reservation_instance = PaymentAfterReservation.from_json(json)
# print the JSON string representation of the object
print PaymentAfterReservation.to_json()

# convert the object into a dict
payment_after_reservation_dict = payment_after_reservation_instance.to_dict()
# create an instance of PaymentAfterReservation from a dict
payment_after_reservation_form_dict = payment_after_reservation.from_dict(payment_after_reservation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


