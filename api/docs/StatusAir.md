# StatusAir


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**OfferStatusEnum**](OfferStatusEnum.md) |  | [optional] 
**flight_refs** | **List[str]** | The flightRefs the status is applicable to within the Offer | [optional] 
**code** | **str** | Status code | [optional] 
**past_date_ind** | **bool** | If true, the flight is considered to be past date | [optional] 

## Example

```python
from openapi_client.models.status_air import StatusAir

# TODO update the JSON string below
json = "{}"
# create an instance of StatusAir from a JSON string
status_air_instance = StatusAir.from_json(json)
# print the JSON string representation of the object
print StatusAir.to_json()

# convert the object into a dict
status_air_dict = status_air_instance.to_dict()
# create an instance of StatusAir from a dict
status_air_form_dict = status_air.from_dict(status_air_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


