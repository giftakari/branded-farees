# RateCandidate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**priority** | **int** | rate candidate priority | [optional] 
**rate_code** | **str** | The rateCode to be applied to the request | [optional] 
**rate_category** | [**RateCategoryEnum**](RateCategoryEnum.md) |  | [optional] 
**chain_code** | **str** | The hotel chain code | [optional] 
**property_code** | **str** | The hotel chain code | [optional] 

## Example

```python
from openapi_client.models.rate_candidate import RateCandidate

# TODO update the JSON string below
json = "{}"
# create an instance of RateCandidate from a JSON string
rate_candidate_instance = RateCandidate.from_json(json)
# print the JSON string representation of the object
print RateCandidate.to_json()

# convert the object into a dict
rate_candidate_dict = rate_candidate_instance.to_dict()
# create an instance of RateCandidate from a dict
rate_candidate_form_dict = rate_candidate.from_dict(rate_candidate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


