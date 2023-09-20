# FareSelectionDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validating_carrier** | **str** | Airline code | [optional] 
**prohibit_min_stay_fares_ind** | **bool** | If present and true, fares with minimum stays will not be returned | [optional] 
**prohibit_max_stay_fares_ind** | **bool** | If present and true, fares with maximum stays will not be returned | [optional] 
**refundable_only_ind** | **bool** | This field is deprecated. Use RefundOptions for refunadability options | [optional] 
**prohibit_advance_purchase_fares_ind** | **bool** | If present and true, fares with advance purchase requirements will not be returned | [optional] 
**prohibit_unbundled_fares_ind** | **bool** |  | [optional] 
**prohibit_refundable_fares_ind** | **bool** | This field is deprecated. Use RefundOptions for refunadability options | [optional] 

## Example

```python
from openapi_client.models.fare_selection_detail import FareSelectionDetail

# TODO update the JSON string below
json = "{}"
# create an instance of FareSelectionDetail from a JSON string
fare_selection_detail_instance = FareSelectionDetail.from_json(json)
# print the JSON string representation of the object
print FareSelectionDetail.to_json()

# convert the object into a dict
fare_selection_detail_dict = fare_selection_detail_instance.to_dict()
# create an instance of FareSelectionDetail from a dict
fare_selection_detail_form_dict = fare_selection_detail.from_dict(fare_selection_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


