# RateCandidatesDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_rate_plans** | **int** | Minimum number rate plans requested in response | [optional] 

## Example

```python
from openapi_client.models.rate_candidates_detail import RateCandidatesDetail

# TODO update the JSON string below
json = "{}"
# create an instance of RateCandidatesDetail from a JSON string
rate_candidates_detail_instance = RateCandidatesDetail.from_json(json)
# print the JSON string representation of the object
print RateCandidatesDetail.to_json()

# convert the object into a dict
rate_candidates_detail_dict = rate_candidates_detail_instance.to_dict()
# create an instance of RateCandidatesDetail from a dict
rate_candidates_detail_form_dict = rate_candidates_detail.from_dict(rate_candidates_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


