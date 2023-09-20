# AgencyServiceFeeResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agency_service_fee** | [**AgencyServiceFeeID**](AgencyServiceFeeID.md) |  | [optional] 

## Example

```python
from openapi_client.models.agency_service_fee_response import AgencyServiceFeeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyServiceFeeResponse from a JSON string
agency_service_fee_response_instance = AgencyServiceFeeResponse.from_json(json)
# print the JSON string representation of the object
print AgencyServiceFeeResponse.to_json()

# convert the object into a dict
agency_service_fee_response_dict = agency_service_fee_response_instance.to_dict()
# create an instance of AgencyServiceFeeResponse from a dict
agency_service_fee_response_form_dict = agency_service_fee_response.from_dict(agency_service_fee_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


