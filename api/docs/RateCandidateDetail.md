# RateCandidateDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_id** | **str** | ID of the rate plan associated with the negotiated rate. | [optional] 
**customer_loyalty** | [**CustomerLoyalty**](CustomerLoyalty.md) |  | [optional] 

## Example

```python
from openapi_client.models.rate_candidate_detail import RateCandidateDetail

# TODO update the JSON string below
json = "{}"
# create an instance of RateCandidateDetail from a JSON string
rate_candidate_detail_instance = RateCandidateDetail.from_json(json)
# print the JSON string representation of the object
print RateCandidateDetail.to_json()

# convert the object into a dict
rate_candidate_detail_dict = rate_candidate_detail_instance.to_dict()
# create an instance of RateCandidateDetail from a dict
rate_candidate_detail_form_dict = rate_candidate_detail.from_dict(rate_candidate_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


