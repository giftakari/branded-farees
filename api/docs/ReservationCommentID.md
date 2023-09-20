# ReservationCommentID


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** | Local indentifier within a given message for this object. | [optional] 

## Example

```python
from openapi_client.models.reservation_comment_id import ReservationCommentID

# TODO update the JSON string below
json = "{}"
# create an instance of ReservationCommentID from a JSON string
reservation_comment_id_instance = ReservationCommentID.from_json(json)
# print the JSON string representation of the object
print ReservationCommentID.to_json()

# convert the object into a dict
reservation_comment_id_dict = reservation_comment_id_instance.to_dict()
# create an instance of ReservationCommentID from a dict
reservation_comment_id_form_dict = reservation_comment_id.from_dict(reservation_comment_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


