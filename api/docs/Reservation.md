# Reservation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer** | [**List[Offer]**](Offer.md) |  | [optional] 
**traveler** | [**List[Traveler]**](Traveler.md) |  | [optional] 
**traveler_product** | [**List[TravelerProduct]**](TravelerProduct.md) |  | [optional] 
**form_of_payment** | [**List[FormOfPaymentID]**](FormOfPaymentID.md) |  | [optional] 
**payment** | [**List[Payment]**](Payment.md) |  | [optional] 
**receipt** | [**List[Receipt]**](Receipt.md) |  | [optional] 
**offer_link** | [**List[OfferLink]**](OfferLink.md) |  | [optional] 
**reservation_comment** | [**List[ReservationComment]**](ReservationComment.md) |  | [optional] 
**primary_contact** | [**List[PrimaryContact]**](PrimaryContact.md) |  | [optional] 
**travel_agency** | [**TravelAgency**](TravelAgency.md) |  | [optional] 
**group_name** | **str** | A name assigned to a Reservation containing an offer with Passengerflight/Flight Quantity equal to or greater than 10 | [optional] 
**special_service** | [**List[SpecialService]**](SpecialService.md) |  | [optional] 
**preference** | [**Preference**](Preference.md) |  | [optional] 
**organization_loyalty_program** | [**List[OrganizationLoyaltyProgram]**](OrganizationLoyaltyProgram.md) |  | [optional] 
**shopping_cart** | [**ShoppingCart**](ShoppingCart.md) |  | [optional] 
**reservation_display_sequence** | [**ReservationDisplaySequence**](ReservationDisplaySequence.md) |  | [optional] 
**agency_service_fee** | [**List[AgencyServiceFee]**](AgencyServiceFee.md) |  | [optional] 
**auto_delete_date** | **date** | The auto delete date represents the date that the Reservation will be kept active. Also known as retention segment or retention date. | [optional] 
**notification_date** | **date** | The notification date represents the date that the Reservation should be reviewed. Also known as ticket time limit date. | [optional] 

## Example

```python
from openapi_client.models.reservation import Reservation

# TODO update the JSON string below
json = "{}"
# create an instance of Reservation from a JSON string
reservation_instance = Reservation.from_json(json)
# print the JSON string representation of the object
print Reservation.to_json()

# convert the object into a dict
reservation_dict = reservation_instance.to_dict()
# create an instance of Reservation from a dict
reservation_form_dict = reservation.from_dict(reservation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


