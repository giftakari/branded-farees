# TicketQueryUpdateTicket


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agency_code** | **str** | Assigned Type: c-1100:AgencyCodeIATA | [optional] 
**date_of_issue** | **date** | Date the ticket was issued | [optional] 
**status** | **str** | Assigned Type: c-1100:StringTiny | 

## Example

```python
from openapi_client.models.ticket_query_update_ticket import TicketQueryUpdateTicket

# TODO update the JSON string below
json = "{}"
# create an instance of TicketQueryUpdateTicket from a JSON string
ticket_query_update_ticket_instance = TicketQueryUpdateTicket.from_json(json)
# print the JSON string representation of the object
print TicketQueryUpdateTicket.to_json()

# convert the object into a dict
ticket_query_update_ticket_dict = ticket_query_update_ticket_instance.to_dict()
# create an instance of TicketQueryUpdateTicket from a dict
ticket_query_update_ticket_form_dict = ticket_query_update_ticket.from_dict(ticket_query_update_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


