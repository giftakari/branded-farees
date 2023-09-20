# AdvancePaymentRequired


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**waver_date** | **str** | Waver date | [optional] 
**payment_after_reservation** | [**PaymentAfterReservation**](PaymentAfterReservation.md) |  | 
**payment_before_departure** | [**PaymentBeforeDeparture**](PaymentBeforeDeparture.md) |  | 
**payment_travel_segment_indicator_atpco** | **int** | The ATPCO paymentgeographic indicator. Example &#x3D; 1st segment over the water between area 2 and 3 | [optional] 
**instant_payment_ind** | **bool** | if true, the Offer must be paid at the same time as the reservation is created | [optional] 
**ealier_applies_ind** | **bool** | If true, the earlier of the payment restrictions apply | [optional] 
**later_applies_ind** | **bool** | If true, the later of the payment restrictions apply | [optional] 

## Example

```python
from openapi_client.models.advance_payment_required import AdvancePaymentRequired

# TODO update the JSON string below
json = "{}"
# create an instance of AdvancePaymentRequired from a JSON string
advance_payment_required_instance = AdvancePaymentRequired.from_json(json)
# print the JSON string representation of the object
print AdvancePaymentRequired.to_json()

# convert the object into a dict
advance_payment_required_dict = advance_payment_required_instance.to_dict()
# create an instance of AdvancePaymentRequired from a dict
advance_payment_required_form_dict = advance_payment_required.from_dict(advance_payment_required_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


