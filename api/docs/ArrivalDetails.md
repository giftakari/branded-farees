# ArrivalDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**carrier** | **str** | Carrier | [optional] 
**flight_number** | **str** | Flight Number | [optional] 
**transportation_code** | [**TransportationCategoryEnum**](TransportationCategoryEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.arrival_details import ArrivalDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ArrivalDetails from a JSON string
arrival_details_instance = ArrivalDetails.from_json(json)
# print the JSON string representation of the object
print ArrivalDetails.to_json()

# convert the object into a dict
arrival_details_dict = arrival_details_instance.to_dict()
# create an instance of ArrivalDetails from a dict
arrival_details_form_dict = arrival_details.from_dict(arrival_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


