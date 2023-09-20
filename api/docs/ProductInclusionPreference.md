# ProductInclusionPreference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**leg_sequence** | **List[int]** | The legSequence value | [optional] 
**classification** | [**List[BrandClassificationEnum]**](BrandClassificationEnum.md) |  | 
**additional_classification** | **List[str]** |  | [optional] 
**exact_match_ind** | **bool** | This indicator is deprecated. The default behavior will be to provide an exact match to the product inclusion preferences | [optional] 
**best_match_ind** | **bool** | If true, the bestMatch will be returned according to the select product inclusions | [optional] 

## Example

```python
from openapi_client.models.product_inclusion_preference import ProductInclusionPreference

# TODO update the JSON string below
json = "{}"
# create an instance of ProductInclusionPreference from a JSON string
product_inclusion_preference_instance = ProductInclusionPreference.from_json(json)
# print the JSON string representation of the object
print ProductInclusionPreference.to_json()

# convert the object into a dict
product_inclusion_preference_dict = product_inclusion_preference_instance.to_dict()
# create an instance of ProductInclusionPreference from a dict
product_inclusion_preference_form_dict = product_inclusion_preference.from_dict(product_inclusion_preference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


