# TicketBasePassenger

The monetary value

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | [optional] 
**currency_code** | **str** | Assigned Type: c-1100:CurrencyCode | [optional] 
**code_authority** | **str** | Assigned Type: c-1100:CodeContext | 
**decimal_place** | **int** | Assigned Type: c-1100:CurrencyMinorUnit | 
**decimal_authority** | **str** | Assigned Type: c-1100:CodeContext | [optional] 
**b_t_ind** | **bool** | If true, this is a bulk ticket fare | [optional] 
**i_t_ind** | **bool** | If true, this is an inclusive tour fare | [optional] 

## Example

```python
from openapi_client.models.ticket_base_passenger import TicketBasePassenger

# TODO update the JSON string below
json = "{}"
# create an instance of TicketBasePassenger from a JSON string
ticket_base_passenger_instance = TicketBasePassenger.from_json(json)
# print the JSON string representation of the object
print TicketBasePassenger.to_json()

# convert the object into a dict
ticket_base_passenger_dict = ticket_base_passenger_instance.to_dict()
# create an instance of TicketBasePassenger from a dict
ticket_base_passenger_form_dict = ticket_base_passenger.from_dict(ticket_base_passenger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


