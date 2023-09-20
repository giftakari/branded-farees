# PaymentAfterReservationDuration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **str** | The advance duration the Offer can be reserved. | 

## Example

```python
from openapi_client.models.payment_after_reservation_duration import PaymentAfterReservationDuration

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentAfterReservationDuration from a JSON string
payment_after_reservation_duration_instance = PaymentAfterReservationDuration.from_json(json)
# print the JSON string representation of the object
print PaymentAfterReservationDuration.to_json()

# convert the object into a dict
payment_after_reservation_duration_dict = payment_after_reservation_duration_instance.to_dict()
# create an instance of PaymentAfterReservationDuration from a dict
payment_after_reservation_duration_form_dict = payment_after_reservation_duration.from_dict(payment_after_reservation_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


