# RateCandidates


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**rate_candidate** | [**List[RateCandidate]**](RateCandidate.md) |  | 
**pre_pay_rates_only_ind** | **bool** | If true, only prepay rates will be returned | [optional] 
**post_pay_rates_only_ind** | **bool** | If true, only postpay rates will be returned | [optional] 

## Example

```python
from openapi_client.models.rate_candidates import RateCandidates

# TODO update the JSON string below
json = "{}"
# create an instance of RateCandidates from a JSON string
rate_candidates_instance = RateCandidates.from_json(json)
# print the JSON string representation of the object
print RateCandidates.to_json()

# convert the object into a dict
rate_candidates_dict = rate_candidates_instance.to_dict()
# create an instance of RateCandidates from a dict
rate_candidates_form_dict = rate_candidates.from_dict(rate_candidates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


