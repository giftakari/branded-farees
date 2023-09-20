# Comment

Textual information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**id** | **str** | Local indentifier within a given message for this object. | [optional] 
**name** | **str** | Title | [optional] 
**language** | **str** | Language code using ISO-639 standard | [optional] 

## Example

```python
from openapi_client.models.comment import Comment

# TODO update the JSON string below
json = "{}"
# create an instance of Comment from a JSON string
comment_instance = Comment.from_json(json)
# print the JSON string representation of the object
print Comment.to_json()

# convert the object into a dict
comment_dict = comment_instance.to_dict()
# create an instance of Comment from a dict
comment_form_dict = comment.from_dict(comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


