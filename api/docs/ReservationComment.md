# ReservationComment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment_source** | [**CommentSourceEnum**](CommentSourceEnum.md) |  | [optional] 
**share_with** | [**ShareWithEnum**](ShareWithEnum.md) |  | [optional] 
**share_with_supplier** | **List[str]** | Reservation comment shared with supplier | [optional] 
**comment** | [**List[Comment]**](Comment.md) |  | [optional] 
**applies_to** | [**List[AppliesTo]**](AppliesTo.md) |  | [optional] 

## Example

```python
from openapi_client.models.reservation_comment import ReservationComment

# TODO update the JSON string below
json = "{}"
# create an instance of ReservationComment from a JSON string
reservation_comment_instance = ReservationComment.from_json(json)
# print the JSON string representation of the object
print ReservationComment.to_json()

# convert the object into a dict
reservation_comment_dict = reservation_comment_instance.to_dict()
# create an instance of ReservationComment from a dict
reservation_comment_form_dict = reservation_comment.from_dict(reservation_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


