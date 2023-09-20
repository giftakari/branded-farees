# ReservationCommentResponseWrapper


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation_comment_response** | [**ReservationCommentResponse**](ReservationCommentResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.reservation_comment_response_wrapper import ReservationCommentResponseWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ReservationCommentResponseWrapper from a JSON string
reservation_comment_response_wrapper_instance = ReservationCommentResponseWrapper.from_json(json)
# print the JSON string representation of the object
print ReservationCommentResponseWrapper.to_json()

# convert the object into a dict
reservation_comment_response_wrapper_dict = reservation_comment_response_wrapper_instance.to_dict()
# create an instance of ReservationCommentResponseWrapper from a dict
reservation_comment_response_wrapper_form_dict = reservation_comment_response_wrapper.from_dict(reservation_comment_response_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


