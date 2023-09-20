# MaximumStayApplies


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maximum_stay_duration** | **str** |  | [optional] 
**maximum_stay_date** | **date** |  | [optional] 
**return_time** | **str** | Return time | [optional] 
**must_commence_by_ind** | **bool** | Indicates if travel must commence by this date/duration | [optional] 
**must_complete_by_ind** | **bool** | Indicates if travel must complete by this date/duration | [optional] 
**from_date_of_issue_ind** | **bool** | If true the Maximum stay is calculated from the date of ticket issuance | [optional] 
**earliest_applies_ind** | **bool** | If true, the earlier of the Maximum stay conditions apply | [optional] 
**latest_applies_ind** | **bool** | If true, the later of the Maximum stay conditions apply | [optional] 

## Example

```python
from openapi_client.models.maximum_stay_applies import MaximumStayApplies

# TODO update the JSON string below
json = "{}"
# create an instance of MaximumStayApplies from a JSON string
maximum_stay_applies_instance = MaximumStayApplies.from_json(json)
# print the JSON string representation of the object
print MaximumStayApplies.to_json()

# convert the object into a dict
maximum_stay_applies_dict = maximum_stay_applies_instance.to_dict()
# create an instance of MaximumStayApplies from a dict
maximum_stay_applies_form_dict = maximum_stay_applies.from_dict(maximum_stay_applies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


