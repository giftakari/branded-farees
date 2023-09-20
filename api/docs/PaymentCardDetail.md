# PaymentCardDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_of_issue** | **str** | The country code ISO | [optional] 
**company_card_reference** | **str** | The company card reference | [optional] 
**bank_name** | **str** | The bank name value | [optional] 
**bank_country_code** | **str** | The bank country code ISO | [optional] 
**bank_state_code** | **str** | The bank state code ISO | [optional] 
**card_holder_id** | [**Identifier**](Identifier.md) |  | [optional] 
**person_name** | [**PersonName**](PersonName.md) |  | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**telephone** | [**List[Telephone]**](Telephone.md) |  | [optional] 
**email** | [**List[Email]**](Email.md) |  | [optional] 
**customer_loyalty** | [**List[CustomerLoyalty]**](CustomerLoyalty.md) |  | [optional] 
**signature_on_file** | [**SignatureOnFile**](SignatureOnFile.md) |  | [optional] 
**three_domain_security** | [**ThreeDomainSecurity**](ThreeDomainSecurity.md) |  | [optional] 
**extended_payment_ind** | **bool** | Implementer: If true, the credit card company is requested to delay the date on which the amount of this transaction is applied to the customer&#39;s account. | [optional] 
**enett_ind** | **bool** | True if this payment card has been issued through Enett | [optional] 
**third_party_ind** | **bool** | If true, then the payment card holder is not one of the travelers in the reservation | [optional] 
**acceptance_override_ind** | **bool** | If true, override airline restriction on the payment card | [optional] 

## Example

```python
from openapi_client.models.payment_card_detail import PaymentCardDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentCardDetail from a JSON string
payment_card_detail_instance = PaymentCardDetail.from_json(json)
# print the JSON string representation of the object
print PaymentCardDetail.to_json()

# convert the object into a dict
payment_card_detail_dict = payment_card_detail_instance.to_dict()
# create an instance of PaymentCardDetail from a dict
payment_card_detail_form_dict = payment_card_detail.from_dict(payment_card_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


