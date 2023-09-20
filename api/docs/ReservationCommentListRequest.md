# ReservationCommentListRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation_comment** | [**List[ReservationComment]**](ReservationComment.md) |  | 

## Example

```python
from openapi_client.models.reservation_comment_list_request import ReservationCommentListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReservationCommentListRequest from a JSON string
reservation_comment_list_request_instance = ReservationCommentListRequest.from_json(json)
# print the JSON string representation of the object
print ReservationCommentListRequest.to_json()

# convert the object into a dict
reservation_comment_list_request_dict = reservation_comment_list_request_instance.to_dict()
# create an instance of ReservationCommentListRequest from a dict
reservation_comment_list_request_form_dict = reservation_comment_list_request.from_dict(reservation_comment_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


