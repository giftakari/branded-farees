# FormOfPaymentVirtualPaymentAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supplier** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**alternate_email_address** | [**List[Email]**](Email.md) | The alternate agency email to be used for correspondence with this virtual payment | [optional] 
**payment_comment** | **str** | Optional text to be sent to the supplier | [optional] 
**alternate_hotel_fax** | [**List[Telephone]**](Telephone.md) | Hotel fax number to be used if the hotel fax is unknown or not provided in Property details | [optional] 
**maximum_chargeable_amount** | [**List[CurrencyAmount]**](CurrencyAmount.md) | The maximum amount that the supplier may charge to the payment card including room rate and any incidentals specified | [optional] 
**incidental_charges** | **List[str]** | List of incidentals that are permitted to be charged to the virtual payment card. | [optional] 

## Example

```python
from openapi_client.models.form_of_payment_virtual_payment_account import FormOfPaymentVirtualPaymentAccount

# TODO update the JSON string below
json = "{}"
# create an instance of FormOfPaymentVirtualPaymentAccount from a JSON string
form_of_payment_virtual_payment_account_instance = FormOfPaymentVirtualPaymentAccount.from_json(json)
# print the JSON string representation of the object
print FormOfPaymentVirtualPaymentAccount.to_json()

# convert the object into a dict
form_of_payment_virtual_payment_account_dict = form_of_payment_virtual_payment_account_instance.to_dict()
# create an instance of FormOfPaymentVirtualPaymentAccount from a dict
form_of_payment_virtual_payment_account_form_dict = form_of_payment_virtual_payment_account.from_dict(form_of_payment_virtual_payment_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


