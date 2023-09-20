# LastReservationDuration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **str** | The advance duration the Offer can be reserved. | 

## Example

```python
from openapi_client.models.last_reservation_duration import LastReservationDuration

# TODO update the JSON string below
json = "{}"
# create an instance of LastReservationDuration from a JSON string
last_reservation_duration_instance = LastReservationDuration.from_json(json)
# print the JSON string representation of the object
print LastReservationDuration.to_json()

# convert the object into a dict
last_reservation_duration_dict = last_reservation_duration_instance.to_dict()
# create an instance of LastReservationDuration from a dict
last_reservation_duration_form_dict = last_reservation_duration.from_dict(last_reservation_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


