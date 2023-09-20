# PaymentCard


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** | Payment card reference ID. | [optional] 
**effective_date** | **date** | Indicated starting date. | [optional] 
**expire_date** | **str** | The expiration date value | [optional] 
**approval_code** | **str** | The approval code value | [optional] 
**privacy_group** | [**Privacy**](Privacy.md) |  | [optional] 
**card_type** | [**PaymentCardTypeEnum**](PaymentCardTypeEnum.md) |  | [optional] 
**card_code** | **str** | Specifies the two character code (MC, VI, AX, etc) for the payment card (open enumeration) | [optional] 
**card_brand** | [**PaymentCardTypeIssuer**](PaymentCardTypeIssuer.md) |  | [optional] 
**card_issuer** | [**PaymentCardTypeIssuer**](PaymentCardTypeIssuer.md) |  | [optional] 
**card_holder_name** | **str** | Name as displayed on Payment Card | [optional] 
**card_number** | [**CardNumber**](CardNumber.md) |  | [optional] 
**series_code** | [**SeriesCode**](SeriesCode.md) |  | [optional] 
**magnetic_stripe** | [**List[MagneticStripe]**](MagneticStripe.md) |  | [optional] 
**secure_ind** | **bool** | Implementer: If true, all or a portion of this data is secure, via tokenization, encryption and/or masking. | [optional] 

## Example

```python
from openapi_client.models.payment_card import PaymentCard

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentCard from a JSON string
payment_card_instance = PaymentCard.from_json(json)
# print the JSON string representation of the object
print PaymentCard.to_json()

# convert the object into a dict
payment_card_dict = payment_card_instance.to_dict()
# create an instance of PaymentCard from a dict
payment_card_form_dict = payment_card.from_dict(payment_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


