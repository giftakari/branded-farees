# AgeQualifying


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**min_age** | **int** | MinAge: The minimum age to qualify for AgeQualifyingCode. | [optional] 
**max_age** | **int** | Max Age: The maximum age to qualify for AgeQualifyingCode. | [optional] 
**age_bucket** | **str** | The age bucket | [optional] 
**count** | **int** | The number of age qualifying | [optional] 
**age_qualifying_code** | **str** | Enter 10 for an adult or 08 for a child | [optional] 

## Example

```python
from openapi_client.models.age_qualifying import AgeQualifying

# TODO update the JSON string below
json = "{}"
# create an instance of AgeQualifying from a JSON string
age_qualifying_instance = AgeQualifying.from_json(json)
# print the JSON string representation of the object
print AgeQualifying.to_json()

# convert the object into a dict
age_qualifying_dict = age_qualifying_instance.to_dict()
# create an instance of AgeQualifying from a dict
age_qualifying_form_dict = age_qualifying.from_dict(age_qualifying_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


