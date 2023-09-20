# TicketPrice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**fare_calculation** | **str** | Calculation of applicable fare | [optional] 
**fare_breakdown** | **str** | An itineraray used as the start and finish of a particular fare | [optional] 
**currency_code** | [**CurrencyCode**](CurrencyCode.md) |  | 
**base** | **float** |  | 
**taxes** | [**PaidTaxes**](PaidTaxes.md) |  | [optional] 
**fees** | [**Fees**](Fees.md) |  | [optional] 
**total** | **float** |  | 
**commission** | [**Commission**](Commission.md) |  | [optional] 
**filed_amount** | [**FiledAmount**](FiledAmount.md) |  | [optional] 
**paid_taxes** | [**Taxes**](Taxes.md) |  | [optional] 
**i_t_fare_ind** | **bool** | if true, this is an IT fare and the base amount is not exposed | [optional] 
**b_t_fare_ind** | **bool** | if true, this is a BT fare and the base amount is not exposed | [optional] 
**additional_collection** | [**FiledAmount**](FiledAmount.md) |  | [optional] 
**net_amount** | [**AlternateAmount**](AlternateAmount.md) |  | [optional] 

## Example

```python
from openapi_client.models.ticket_price import TicketPrice

# TODO update the JSON string below
json = "{}"
# create an instance of TicketPrice from a JSON string
ticket_price_instance = TicketPrice.from_json(json)
# print the JSON string representation of the object
print TicketPrice.to_json()

# convert the object into a dict
ticket_price_dict = ticket_price_instance.to_dict()
# create an instance of TicketPrice from a dict
ticket_price_form_dict = ticket_price.from_dict(ticket_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


