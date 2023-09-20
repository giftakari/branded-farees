# BrandAttributeInclusion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**leg_sequence** | **List[int]** | the leg sequence | [optional] 
**classification** | [**List[BrandClassificationEnum]**](BrandClassificationEnum.md) |  | [optional] 
**additional_classification** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.brand_attribute_inclusion import BrandAttributeInclusion

# TODO update the JSON string below
json = "{}"
# create an instance of BrandAttributeInclusion from a JSON string
brand_attribute_inclusion_instance = BrandAttributeInclusion.from_json(json)
# print the JSON string representation of the object
print BrandAttributeInclusion.to_json()

# convert the object into a dict
brand_attribute_inclusion_dict = brand_attribute_inclusion_instance.to_dict()
# create an instance of BrandAttributeInclusion from a dict
brand_attribute_inclusion_form_dict = brand_attribute_inclusion.from_dict(brand_attribute_inclusion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


