# PaymentCardTypeIssuer

This object contains Cards details for Payment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_card_issuers** | [**ListPaymentCardIssuerEnum**](ListPaymentCardIssuerEnum.md) |  | [optional] 
**payment_card_issuers_extension** | **str** |  | [optional] 
**issue_number** | **int** | Assigned Type: c-1100:NumberDoubleDigit | [optional] 

## Example

```python
from openapi_client.models.payment_card_type_issuer import PaymentCardTypeIssuer

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentCardTypeIssuer from a JSON string
payment_card_type_issuer_instance = PaymentCardTypeIssuer.from_json(json)
# print the JSON string representation of the object
print PaymentCardTypeIssuer.to_json()

# convert the object into a dict
payment_card_type_issuer_dict = payment_card_type_issuer_instance.to_dict()
# create an instance of PaymentCardTypeIssuer from a dict
payment_card_type_issuer_form_dict = payment_card_type_issuer.from_dict(payment_card_type_issuer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


