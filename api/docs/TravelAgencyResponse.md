# TravelAgencyResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**travel_agency** | [**TravelAgencyID**](TravelAgencyID.md) |  | [optional] 

## Example

```python
from openapi_client.models.travel_agency_response import TravelAgencyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TravelAgencyResponse from a JSON string
travel_agency_response_instance = TravelAgencyResponse.from_json(json)
# print the JSON string representation of the object
print TravelAgencyResponse.to_json()

# convert the object into a dict
travel_agency_response_dict = travel_agency_response_instance.to_dict()
# create an instance of TravelAgencyResponse from a dict
travel_agency_response_form_dict = travel_agency_response.from_dict(travel_agency_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


