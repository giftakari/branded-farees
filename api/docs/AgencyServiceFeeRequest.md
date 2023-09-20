# AgencyServiceFeeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agency_service_fee** | [**AgencyServiceFee**](AgencyServiceFee.md) |  | [optional] 

## Example

```python
from openapi_client.models.agency_service_fee_request import AgencyServiceFeeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyServiceFeeRequest from a JSON string
agency_service_fee_request_instance = AgencyServiceFeeRequest.from_json(json)
# print the JSON string representation of the object
print AgencyServiceFeeRequest.to_json()

# convert the object into a dict
agency_service_fee_request_dict = agency_service_fee_request_instance.to_dict()
# create an instance of AgencyServiceFeeRequest from a dict
agency_service_fee_request_form_dict = agency_service_fee_request.from_dict(agency_service_fee_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


