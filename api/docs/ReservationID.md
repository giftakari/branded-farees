# ReservationID


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** | Internal ID | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.reservation_id import ReservationID

# TODO update the JSON string below
json = "{}"
# create an instance of ReservationID from a JSON string
reservation_id_instance = ReservationID.from_json(json)
# print the JSON string representation of the object
print ReservationID.to_json()

# convert the object into a dict
reservation_id_dict = reservation_id_instance.to_dict()
# create an instance of ReservationID from a dict
reservation_id_form_dict = reservation_id.from_dict(reservation_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


