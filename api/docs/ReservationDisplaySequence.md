# ReservationDisplaySequence


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**display_sequence** | [**List[DisplaySequence]**](DisplaySequence.md) |  | [optional] 
**auto_delete_date_sequence** | **int** | The sequence of the autoDeleteDate (retention segment) within the Reservation | [optional] 

## Example

```python
from openapi_client.models.reservation_display_sequence import ReservationDisplaySequence

# TODO update the JSON string below
json = "{}"
# create an instance of ReservationDisplaySequence from a JSON string
reservation_display_sequence_instance = ReservationDisplaySequence.from_json(json)
# print the JSON string representation of the object
print ReservationDisplaySequence.to_json()

# convert the object into a dict
reservation_display_sequence_dict = reservation_display_sequence_instance.to_dict()
# create an instance of ReservationDisplaySequence from a dict
reservation_display_sequence_form_dict = reservation_display_sequence.from_dict(reservation_display_sequence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


