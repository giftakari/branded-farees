# PricingModifiersAir


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**currency_code** | **str** | Currency Code ISO | [optional] 
**fare_selection** | [**FareSelectionDetail**](FareSelectionDetail.md) |  | [optional] 
**organization_information** | [**OrganizationInformation**](OrganizationInformation.md) |  | [optional] 
**tax_exemption** | [**TaxExemption**](TaxExemption.md) |  | [optional] 
**promotional_code** | [**List[PromotionalCode]**](PromotionalCode.md) |  | [optional] 
**sell_city** | **str** | Overrides the sell city of the requestor. | [optional] 
**ticket_city** | **str** | Overrides the ticket city of the requestor. | [optional] 
**pricing_pcc** | **str** |  | [optional] 
**ticketing_pcc** | **str** |  | [optional] 
**include_split_payment_ind** | **bool** | If true, split payment (split ticket) offerings/offers will be returned | [optional] 
**return_most_restrictive_brand_ind** | **bool** | if true, the most restrictive brand will be returned in the response when there are different brands present in the Offering | [optional] 
**split_payment_offerings** | **float** | The percentage, between 0 and 99, of round trip offerings the user would like returned in the result set. | [optional] 

## Example

```python
from openapi_client.models.pricing_modifiers_air import PricingModifiersAir

# TODO update the JSON string below
json = "{}"
# create an instance of PricingModifiersAir from a JSON string
pricing_modifiers_air_instance = PricingModifiersAir.from_json(json)
# print the JSON string representation of the object
print PricingModifiersAir.to_json()

# convert the object into a dict
pricing_modifiers_air_dict = pricing_modifiers_air_instance.to_dict()
# create an instance of PricingModifiersAir from a dict
pricing_modifiers_air_form_dict = pricing_modifiers_air.from_dict(pricing_modifiers_air_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


