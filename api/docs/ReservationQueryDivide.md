# ReservationQueryDivide


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation_identifier** | [**ReservationIdentifier**](ReservationIdentifier.md) |  | 
**traveler_identifier** | [**List[TravelerIdentifier]**](TravelerIdentifier.md) |  | 

## Example

```python
from openapi_client.models.reservation_query_divide import ReservationQueryDivide

# TODO update the JSON string below
json = "{}"
# create an instance of ReservationQueryDivide from a JSON string
reservation_query_divide_instance = ReservationQueryDivide.from_json(json)
# print the JSON string representation of the object
print ReservationQueryDivide.to_json()

# convert the object into a dict
reservation_query_divide_dict = reservation_query_divide_instance.to_dict()
# create an instance of ReservationQueryDivide from a dict
reservation_query_divide_form_dict = reservation_query_divide.from_dict(reservation_query_divide_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


