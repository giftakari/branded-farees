# PaymentCriteria


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**issuer_identification_number** | **str** | This the BIN/IIN | [optional] 
**payment_card_code** | **str** | A two character code for a credit card, like MC, AX | [optional] 
**document_number** | [**List[DocumentNumber]**](DocumentNumber.md) |  | [optional] 
**agency_account_ind** | **bool** | If true, payment will be made by agency account | [optional] 
**bsp_ind** | **bool** | If true, payment will be made by BSP | [optional] 
**cash_ind** | **bool** | If true, payment will be made by cash | [optional] 
**invoice_ind** | **bool** | If true, payment will be made by invoice | [optional] 

## Example

```python
from openapi_client.models.payment_criteria import PaymentCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentCriteria from a JSON string
payment_criteria_instance = PaymentCriteria.from_json(json)
# print the JSON string representation of the object
print PaymentCriteria.to_json()

# convert the object into a dict
payment_criteria_dict = payment_criteria_instance.to_dict()
# create an instance of PaymentCriteria from a dict
payment_criteria_form_dict = payment_criteria.from_dict(payment_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


