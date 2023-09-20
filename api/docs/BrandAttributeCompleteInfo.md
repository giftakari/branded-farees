# BrandAttributeCompleteInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Assigned Type: ctbr-1100:BrandAttributeName | [optional] 
**attribute_text** | [**List[BrandText]**](BrandText.md) |  | 

## Example

```python
from openapi_client.models.brand_attribute_complete_info import BrandAttributeCompleteInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BrandAttributeCompleteInfo from a JSON string
brand_attribute_complete_info_instance = BrandAttributeCompleteInfo.from_json(json)
# print the JSON string representation of the object
print BrandAttributeCompleteInfo.to_json()

# convert the object into a dict
brand_attribute_complete_info_dict = brand_attribute_complete_info_instance.to_dict()
# create an instance of BrandAttributeCompleteInfo from a dict
brand_attribute_complete_info_form_dict = brand_attribute_complete_info.from_dict(brand_attribute_complete_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


