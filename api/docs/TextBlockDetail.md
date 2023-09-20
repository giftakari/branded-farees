# TextBlockDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sequence** | **int** | The order of the text block, if there are more than one block. | [optional] 
**description** | **str** | Text block detail description | [optional] 
**image** | [**Image**](Image.md) |  | [optional] 
**url** | **str** | A URL for this block | [optional] 
**date_create_modify** | [**DateCreateModify**](DateCreateModify.md) |  | 

## Example

```python
from openapi_client.models.text_block_detail import TextBlockDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TextBlockDetail from a JSON string
text_block_detail_instance = TextBlockDetail.from_json(json)
# print the JSON string representation of the object
print TextBlockDetail.to_json()

# convert the object into a dict
text_block_detail_dict = text_block_detail_instance.to_dict()
# create an instance of TextBlockDetail from a dict
text_block_detail_form_dict = text_block_detail.from_dict(text_block_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


