# AgencyServiceFee


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry_date** | **datetime** | The service fee expiry date. Once expiry date has been reached, the service fee information will only be stored in the ReservationReceipt | [optional] 
**description** | **str** | The description of the service fee | [optional] 
**amount** | [**CurrencyAmount**](CurrencyAmount.md) |  | 
**tax** | [**List[Tax]**](Tax.md) |  | [optional] 
**related_document_number** | [**DocumentNumber**](DocumentNumber.md) |  | [optional] 
**traveler_ref** | **str** | Reference to a Traveler within the Reservation that this service fee applies to | [optional] 
**offer_ref** | **str** | Reference to an Offer within the Reservation that this service fee applies to | [optional] 

## Example

```python
from openapi_client.models.agency_service_fee import AgencyServiceFee

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyServiceFee from a JSON string
agency_service_fee_instance = AgencyServiceFee.from_json(json)
# print the JSON string representation of the object
print AgencyServiceFee.to_json()

# convert the object into a dict
agency_service_fee_dict = agency_service_fee_instance.to_dict()
# create an instance of AgencyServiceFee from a dict
agency_service_fee_form_dict = agency_service_fee.from_dict(agency_service_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


