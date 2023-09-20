# TextFormatted

Provides text and indicates whether it is formatted or not.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**language** | **str** | The language in which the text is provided. | [optional] 
**text_format** | [**TextFormatEnum**](TextFormatEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.text_formatted import TextFormatted

# TODO update the JSON string below
json = "{}"
# create an instance of TextFormatted from a JSON string
text_formatted_instance = TextFormatted.from_json(json)
# print the JSON string representation of the object
print TextFormatted.to_json()

# convert the object into a dict
text_formatted_dict = text_formatted_instance.to_dict()
# create an instance of TextFormatted from a dict
text_formatted_form_dict = text_formatted.from_dict(text_formatted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


