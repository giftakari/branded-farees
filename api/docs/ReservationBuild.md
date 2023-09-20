# ReservationBuild


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**traveler** | [**List[TravelerID]**](TravelerID.md) |  | 
**form_of_payment** | [**List[FormOfPaymentID]**](FormOfPaymentID.md) |  | [optional] 
**payment** | [**List[PaymentID]**](PaymentID.md) |  | [optional] 
**reservation_comment** | [**List[ReservationCommentID]**](ReservationCommentID.md) |  | [optional] 
**primary_contact** | [**List[PrimaryContactID]**](PrimaryContactID.md) |  | [optional] 
**special_service** | [**List[SpecialServiceID]**](SpecialServiceID.md) |  | [optional] 
**accounting** | [**AccountingID**](AccountingID.md) |  | [optional] 
**document_overrides** | [**List[DocumentOverridesID]**](DocumentOverridesID.md) |  | [optional] 
**preference** | [**List[PreferenceID]**](PreferenceID.md) |  | [optional] 
**receipt_confirmation** | [**ReceiptConfirmation**](ReceiptConfirmation.md) |  | [optional] 
**travel_agency** | [**TravelAgency**](TravelAgency.md) |  | [optional] 

## Example

```python
from openapi_client.models.reservation_build import ReservationBuild

# TODO update the JSON string below
json = "{}"
# create an instance of ReservationBuild from a JSON string
reservation_build_instance = ReservationBuild.from_json(json)
# print the JSON string representation of the object
print ReservationBuild.to_json()

# convert the object into a dict
reservation_build_dict = reservation_build_instance.to_dict()
# create an instance of ReservationBuild from a dict
reservation_build_form_dict = reservation_build.from_dict(reservation_build_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


