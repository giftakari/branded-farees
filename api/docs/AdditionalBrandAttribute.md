# AdditionalBrandAttribute


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**classification** | **str** | The Travelport classification used for categories of ancillaries | 
**inclusion** | [**BrandInclusionEnum**](BrandInclusionEnum.md) |  | 
**image_url** | **List[str]** |  | [optional] 
**matched_attribute_ind** | **bool** | If true, this is a matched attribute | [optional] 
**group_code** | **str** |  | [optional] 
**sub_group_code** | **str** |  | [optional] 
**sub_code** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.additional_brand_attribute import AdditionalBrandAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalBrandAttribute from a JSON string
additional_brand_attribute_instance = AdditionalBrandAttribute.from_json(json)
# print the JSON string representation of the object
print AdditionalBrandAttribute.to_json()

# convert the object into a dict
additional_brand_attribute_dict = additional_brand_attribute_instance.to_dict()
# create an instance of AdditionalBrandAttribute from a dict
additional_brand_attribute_form_dict = additional_brand_attribute.from_dict(additional_brand_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


