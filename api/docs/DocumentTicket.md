# DocumentTicket


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**control_number** | **str** | The control number assigned to the Ticket | 
**historic_ind** | **bool** | If true, this document has been superseded by a new Document facet and may have been exchanged, voided or refunded | [optional] 

## Example

```python
from openapi_client.models.document_ticket import DocumentTicket

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentTicket from a JSON string
document_ticket_instance = DocumentTicket.from_json(json)
# print the JSON string representation of the object
print DocumentTicket.to_json()

# convert the object into a dict
document_ticket_dict = document_ticket_instance.to_dict()
# create an instance of DocumentTicket from a dict
document_ticket_form_dict = document_ticket.from_dict(document_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


