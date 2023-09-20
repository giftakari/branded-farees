# DepartureDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminal** | **str** | Departure/Arrival terminal | [optional] 
**country** | **str** | Country of to departure or arrival | [optional] 

## Example

```python
from openapi_client.models.departure_detail import DepartureDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DepartureDetail from a JSON string
departure_detail_instance = DepartureDetail.from_json(json)
# print the JSON string representation of the object
print DepartureDetail.to_json()

# convert the object into a dict
departure_detail_dict = departure_detail_instance.to_dict()
# create an instance of DepartureDetail from a dict
departure_detail_form_dict = departure_detail.from_dict(departure_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


