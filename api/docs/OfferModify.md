# OfferModify


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_identifier** | [**OfferIdentifier**](OfferIdentifier.md) |  | [optional] 
**modify_price** | [**ModifyPriceDetail**](ModifyPriceDetail.md) |  | 
**schedule_change_ind** | **bool** | If true the Offer_Modify is as a result of an airline initiated schedule change | [optional] 
**retained_value_ind** | **bool** | If true, the value will be retained on a document for future use | [optional] 
**products_updated_ind** | **bool** | If present and true, the products in the host copy of the reservation have already been updated | [optional] 
**price_updated_ind** | **bool** | If present and true, the price in the host copy of the reservation has already been updated | [optional] 
**supplier_retained_price** | [**PriceDetail**](PriceDetail.md) |  | [optional] 
**consumed_price** | [**PriceDetail**](PriceDetail.md) |  | [optional] 

## Example

```python
from openapi_client.models.offer_modify import OfferModify

# TODO update the JSON string below
json = "{}"
# create an instance of OfferModify from a JSON string
offer_modify_instance = OfferModify.from_json(json)
# print the JSON string representation of the object
print OfferModify.to_json()

# convert the object into a dict
offer_modify_dict = offer_modify_instance.to_dict()
# create an instance of OfferModify from a dict
offer_modify_form_dict = offer_modify.from_dict(offer_modify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


