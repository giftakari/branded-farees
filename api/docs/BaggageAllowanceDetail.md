# BaggageAllowanceDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Url for the airline&#39;s baggage information web site | [optional] 

## Example

```python
from openapi_client.models.baggage_allowance_detail import BaggageAllowanceDetail

# TODO update the JSON string below
json = "{}"
# create an instance of BaggageAllowanceDetail from a JSON string
baggage_allowance_detail_instance = BaggageAllowanceDetail.from_json(json)
# print the JSON string representation of the object
print BaggageAllowanceDetail.to_json()

# convert the object into a dict
baggage_allowance_detail_dict = baggage_allowance_detail_instance.to_dict()
# create an instance of BaggageAllowanceDetail from a dict
baggage_allowance_detail_form_dict = baggage_allowance_detail.from_dict(baggage_allowance_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


