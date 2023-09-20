# ArrivalDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminal** | **str** | Departure/Arrival terminal | [optional] 
**country** | **str** | Country of to departure or arrival | [optional] 

## Example

```python
from openapi_client.models.arrival_detail import ArrivalDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ArrivalDetail from a JSON string
arrival_detail_instance = ArrivalDetail.from_json(json)
# print the JSON string representation of the object
print ArrivalDetail.to_json()

# convert the object into a dict
arrival_detail_dict = arrival_detail_instance.to_dict()
# create an instance of ArrivalDetail from a dict
arrival_detail_form_dict = arrival_detail.from_dict(arrival_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


