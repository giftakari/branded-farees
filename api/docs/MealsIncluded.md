# MealsIncluded

Indicates if a meal is included or not

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breakfast_ind** | **bool** |  | [optional] 
**lunch_ind** | **bool** |  | [optional] 
**dinner_ind** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.meals_included import MealsIncluded

# TODO update the JSON string below
json = "{}"
# create an instance of MealsIncluded from a JSON string
meals_included_instance = MealsIncluded.from_json(json)
# print the JSON string representation of the object
print MealsIncluded.to_json()

# convert the object into a dict
meals_included_dict = meals_included_instance.to_dict()
# create an instance of MealsIncluded from a dict
meals_included_form_dict = meals_included.from_dict(meals_included_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


