# TextTitleAndDescription

Descriptive text

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**languages** | **List[str]** | Language of the text | [optional] 
**title** | **str** | Title of the Text | [optional] 

## Example

```python
from openapi_client.models.text_title_and_description import TextTitleAndDescription

# TODO update the JSON string below
json = "{}"
# create an instance of TextTitleAndDescription from a JSON string
text_title_and_description_instance = TextTitleAndDescription.from_json(json)
# print the JSON string representation of the object
print TextTitleAndDescription.to_json()

# convert the object into a dict
text_title_and_description_dict = text_title_and_description_instance.to_dict()
# create an instance of TextTitleAndDescription from a dict
text_title_and_description_form_dict = text_title_and_description.from_dict(text_title_and_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


