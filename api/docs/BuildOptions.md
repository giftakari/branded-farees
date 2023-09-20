# BuildOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**max_number_of_upsells_to_return** | **int** | NonnegativeInteger | [optional] 
**payment_criteria** | [**PaymentCriteria**](PaymentCriteria.md) |  | [optional] 
**fare_rule_type** | [**FareRuleEnum**](FareRuleEnum.md) |  | [optional] 
**fare_rule_category** | [**List[FareRuleCategoryEnum]**](FareRuleCategoryEnum.md) |  | [optional] 
**return_branded_fares_ind** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.build_options import BuildOptions

# TODO update the JSON string below
json = "{}"
# create an instance of BuildOptions from a JSON string
build_options_instance = BuildOptions.from_json(json)
# print the JSON string representation of the object
print BuildOptions.to_json()

# convert the object into a dict
build_options_dict = build_options_instance.to_dict()
# create an instance of BuildOptions from a dict
build_options_form_dict = build_options.from_dict(build_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


