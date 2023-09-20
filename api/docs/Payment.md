# Payment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**CurrencyAmount**](CurrencyAmount.md) |  | 
**form_of_payment_identifier** | [**FormOfPaymentIdentifier**](FormOfPaymentIdentifier.md) |  | [optional] 
**offer_identifier** | [**List[OfferIdentifier]**](OfferIdentifier.md) |  | [optional] 
**fees** | [**Fees**](Fees.md) |  | [optional] 
**taxes** | [**Taxes**](Taxes.md) |  | [optional] 
**traveler_identifier_ref** | [**List[TravelerIdentifierRef]**](TravelerIdentifierRef.md) |  | [optional] 
**base_amount** | [**CurrencyAmount**](CurrencyAmount.md) |  | [optional] 
**deposit_ind** | **bool** | If true, the payment is a deposit on the referenced Offer | [optional] 
**extended_payment** | [**ExtendedPayment**](ExtendedPayment.md) |  | [optional] 
**agency_service_fee_identifier** | [**List[AgencyServiceFeeIdentifier]**](AgencyServiceFeeIdentifier.md) |  | [optional] 
**guarantee_ind** | **bool** | If true, the payment is a guarantee for the referenced Offer | [optional] 

## Example

```python
from openapi_client.models.payment import Payment

# TODO update the JSON string below
json = "{}"
# create an instance of Payment from a JSON string
payment_instance = Payment.from_json(json)
# print the JSON string representation of the object
print Payment.to_json()

# convert the object into a dict
payment_dict = payment_instance.to_dict()
# create an instance of Payment from a dict
payment_form_dict = payment.from_dict(payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


