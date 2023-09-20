# TermsAndConditionsFullHospitality


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guarantee** | [**List[Guarantee]**](Guarantee.md) |  | [optional] 
**cancel_penalty** | [**List[CancelPenalty]**](CancelPenalty.md) |  | [optional] 
**accepted_credit_card** | [**List[AcceptedCreditCard]**](AcceptedCreditCard.md) |  | [optional] 
**description** | **List[str]** |  | [optional] 
**meals_included** | [**MealsIncluded**](MealsIncluded.md) |  | [optional] 
**product_rate_code_info** | [**List[ProductRateCodeInfo]**](ProductRateCodeInfo.md) |  | [optional] 
**check_in_out_policy** | [**CheckInOutPolicy**](CheckInOutPolicy.md) |  | [optional] 
**deposit_policy** | [**DepositPolicy**](DepositPolicy.md) |  | [optional] 
**rate_payment_info** | [**RatePaymentEnum**](RatePaymentEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.terms_and_conditions_full_hospitality import TermsAndConditionsFullHospitality

# TODO update the JSON string below
json = "{}"
# create an instance of TermsAndConditionsFullHospitality from a JSON string
terms_and_conditions_full_hospitality_instance = TermsAndConditionsFullHospitality.from_json(json)
# print the JSON string representation of the object
print TermsAndConditionsFullHospitality.to_json()

# convert the object into a dict
terms_and_conditions_full_hospitality_dict = terms_and_conditions_full_hospitality_instance.to_dict()
# create an instance of TermsAndConditionsFullHospitality from a dict
terms_and_conditions_full_hospitality_form_dict = terms_and_conditions_full_hospitality.from_dict(terms_and_conditions_full_hospitality_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


