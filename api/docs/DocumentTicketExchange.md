# DocumentTicketExchange


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exchange_ind** | **bool** | If true this document has been exchanged for a new document | [optional] 
**historic_ind** | **bool** | if true this document exchange has been cancelled/voided | [optional] 

## Example

```python
from openapi_client.models.document_ticket_exchange import DocumentTicketExchange

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentTicketExchange from a JSON string
document_ticket_exchange_instance = DocumentTicketExchange.from_json(json)
# print the JSON string representation of the object
print DocumentTicketExchange.to_json()

# convert the object into a dict
document_ticket_exchange_dict = document_ticket_exchange_instance.to_dict()
# create an instance of DocumentTicketExchange from a dict
document_ticket_exchange_form_dict = document_ticket_exchange.from_dict(document_ticket_exchange_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


