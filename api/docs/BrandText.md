# BrandText


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** | Internally referenced id | [optional] 
**target** | [**BrandTargetEnum**](BrandTargetEnum.md) |  | [optional] 
**text_formatted** | [**List[TextFormatted]**](TextFormatted.md) |  | 

## Example

```python
from openapi_client.models.brand_text import BrandText

# TODO update the JSON string below
json = "{}"
# create an instance of BrandText from a JSON string
brand_text_instance = BrandText.from_json(json)
# print the JSON string representation of the object
print BrandText.to_json()

# convert the object into a dict
brand_text_dict = brand_text_instance.to_dict()
# create an instance of BrandText from a dict
brand_text_form_dict = brand_text.from_dict(brand_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


