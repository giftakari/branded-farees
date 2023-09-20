# ReservationIdentifier


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **str** | Internal ID | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.reservation_identifier import ReservationIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of ReservationIdentifier from a JSON string
reservation_identifier_instance = ReservationIdentifier.from_json(json)
# print the JSON string representation of the object
print ReservationIdentifier.to_json()

# convert the object into a dict
reservation_identifier_dict = reservation_identifier_instance.to_dict()
# create an instance of ReservationIdentifier from a dict
reservation_identifier_form_dict = reservation_identifier.from_dict(reservation_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


