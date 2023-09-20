# TicketNumber

The ticketNumber that will be used as partial payment for this Offer/Offering

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Ticket number | [optional] 
**ticket_issuer** | **str** | Ticket issuer | [optional] 

## Example

```python
from openapi_client.models.ticket_number import TicketNumber

# TODO update the JSON string below
json = "{}"
# create an instance of TicketNumber from a JSON string
ticket_number_instance = TicketNumber.from_json(json)
# print the JSON string representation of the object
print TicketNumber.to_json()

# convert the object into a dict
ticket_number_dict = ticket_number_instance.to_dict()
# create an instance of TicketNumber from a dict
ticket_number_form_dict = ticket_number.from_dict(ticket_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


