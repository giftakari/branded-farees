# BrandTextDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sequence** | **int** | The order of the text block, if there are more than one block. | [optional] 
**description** | **str** | Assigned Type: c-1100:Description | [optional] 
**image** | [**Image**](Image.md) |  | [optional] 
**url** | **str** | A URL for this block | [optional] 
**date_create_modify** | [**DateCreateModify**](DateCreateModify.md) |  | 

## Example

```python
from openapi_client.models.brand_text_detail import BrandTextDetail

# TODO update the JSON string below
json = "{}"
# create an instance of BrandTextDetail from a JSON string
brand_text_detail_instance = BrandTextDetail.from_json(json)
# print the JSON string representation of the object
print BrandTextDetail.to_json()

# convert the object into a dict
brand_text_detail_dict = brand_text_detail_instance.to_dict()
# create an instance of BrandTextDetail from a dict
brand_text_detail_form_dict = brand_text_detail.from_dict(brand_text_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


