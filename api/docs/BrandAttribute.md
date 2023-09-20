# BrandAttribute


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**classification** | [**BrandClassificationEnum**](BrandClassificationEnum.md) |  | 
**inclusion** | [**BrandInclusionEnum**](BrandInclusionEnum.md) |  | 
**image_url** | **List[str]** |  | [optional] 
**matched_attribute_ind** | **bool** | if true, this is a matched attribute. | [optional] 
**group_code** | **str** |  | [optional] 
**sub_group_code** | **str** |  | [optional] 
**sub_code** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.brand_attribute import BrandAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of BrandAttribute from a JSON string
brand_attribute_instance = BrandAttribute.from_json(json)
# print the JSON string representation of the object
print BrandAttribute.to_json()

# convert the object into a dict
brand_attribute_dict = brand_attribute_instance.to_dict()
# create an instance of BrandAttribute from a dict
brand_attribute_form_dict = brand_attribute.from_dict(brand_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


